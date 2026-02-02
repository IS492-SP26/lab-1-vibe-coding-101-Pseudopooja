import pygame
import sys
import random
import math

# --- Constants ---
# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# Colors (R, G, B)
DARK_BLUE = (0, 20, 40)
YELLOW = (255, 255, 0)

# Paddle dimensions
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

# Ball dimensions
BALL_SIZE = 15

# Speeds
PADDLE_SPEED = 7
AI_PADDLE_SPEED = 6 # AI is slightly slower to make it beatable
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create starfield
class Star:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH)
        self.y = random.randint(0, WINDOW_HEIGHT)
        self.z = random.randint(1, WINDOW_WIDTH) # Star's depth
        self.pz = self.z # Previous depth
        self.brightness = random.randint(100, 255)
        self.twinkle_speed = random.uniform(0.05, 0.2)
        self.twinkle_phase = random.uniform(0, 6.28)
        self.speed = 2

    def update(self):
        self.z -= self.speed
        if self.z < 1:
            self.z = WINDOW_WIDTH
            self.x = random.randint(0, WINDOW_WIDTH)
            self.y = random.randint(0, WINDOW_HEIGHT)
            self.pz = self.z

        self.twinkle_phase += self.twinkle_speed
        self.brightness = int(150 + 105 * ((1 + math.sin(self.twinkle_phase)) / 2))

    def draw(self, win):
        sx = (self.x - WINDOW_WIDTH / 2) * (WINDOW_WIDTH / self.z) + WINDOW_WIDTH / 2
        sy = (self.y - WINDOW_HEIGHT / 2) * (WINDOW_WIDTH / self.z) + WINDOW_HEIGHT / 2
        
        radius = (1 - self.z / WINDOW_WIDTH) * 3
        
        # Draw a line for the trailing effect
        px = (self.x - WINDOW_WIDTH / 2) * (WINDOW_WIDTH / self.pz) + WINDOW_WIDTH / 2
        py = (self.y - WINDOW_HEIGHT / 2) * (WINDOW_WIDTH / self.pz) + WINDOW_HEIGHT / 2
        self.pz = self.z
        
        # Fading trail
        trail_color = (self.brightness * 0.5, self.brightness * 0.5, self.brightness * 0.4)
        pygame.draw.line(win, trail_color, (px, py), (sx, sy))
        
        # Star itself
        color = (self.brightness, self.brightness, self.brightness * 0.8)
        pygame.draw.circle(win, color, (int(sx), int(sy)), int(radius))

stars = [Star() for _ in range(150)]

# Impact particles
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-8, 8)
        self.vy = random.uniform(-8, 8)
        self.lifetime = 30
        self.max_lifetime = 30
        self.color = (random.randint(100, 255), random.randint(150, 255), 255)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.3  # gravity
        self.lifetime -= 1
        self.vx *= 0.98  # friction

    def draw(self, win):
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        size = max(1, int(3 * (self.lifetime / self.max_lifetime)))
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), size)

    def is_alive(self):
        return self.lifetime > 0

particles = []
# --- Screen Shake ---
shake_intensity = 0
shake_duration = 0

def trigger_shake(intensity, duration):
    global shake_intensity, shake_duration
    shake_intensity = intensity
    shake_duration = duration
    
def create_impact(x, y, num_particles=15):
    for _ in range(num_particles):
        particles.append(Particle(x, y))

# --- Main Game Setup ---
def game():
    """
    Main function to initialize and run the Pong game.
    """
    global shake_duration, shake_intensity
    # 1. Initialize Pygame
    pygame.init()

    # 2. Create the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Gemini Pong - Single Player")

    # 3. Create game objects (paddles and ball)
    # pygame.Rect(left, top, width, height)
    paddle_player = pygame.Rect(30, WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_ai = pygame.Rect(WINDOW_WIDTH - 30 - PADDLE_WIDTH, WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WINDOW_WIDTH / 2 - BALL_SIZE / 2, WINDOW_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)

    # 4. Ball movement direction variables
    ball_vel_x = BALL_SPEED_X
    ball_vel_y = BALL_SPEED_Y

    # 5. Score variables
    score_player1 = 0
    score_player2 = 0
    font = pygame.font.SysFont("Arial", 74) # Font for displaying score
    small_font = pygame.font.SysFont("Arial", 36) # Font for labels
    hit_counter = 0

    # 6. Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # --- Game Loop ---
    running = True
    while running:
        # 7. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 8. Key press handling for player paddle movement
        keys = pygame.key.get_pressed()
        # Player 1 paddle (W for up, S for down)
        if keys[pygame.K_w] and paddle_player.top > 0:
            paddle_player.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_player.bottom < WINDOW_HEIGHT:
            paddle_player.y += PADDLE_SPEED
            
        # Player 2 paddle (Up for up, Down for down)
        if keys[pygame.K_UP] and paddle_ai.top > 0:
            paddle_ai.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_ai.bottom < WINDOW_HEIGHT:
            paddle_ai.y += PADDLE_SPEED

        # 10. Ball Movement
        ball.x += ball_vel_x
        ball.y += ball_vel_y

        # 11. Ball Collision Detection
        # a) Collision with top/bottom walls
        if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
            ball_vel_y *= -1 # Reverse vertical direction

        # b) Collision with paddles
        if ball.colliderect(paddle_player):
            ball_vel_x *= -1 # Reverse horizontal direction
            create_impact(ball.centerx, ball.centery)
            trigger_shake(10, 10)
            hit_counter += 1
            if hit_counter >= 3:
                ball_vel_x += math.copysign(0.5, ball_vel_x)
                ball_vel_y += math.copysign(0.5, ball_vel_y)
                hit_counter = 0
            # Move ball out of paddle to prevent sticking
            ball.left = paddle_player.right

        if ball.colliderect(paddle_ai):
            ball_vel_x *= -1 # Reverse horizontal direction
            create_impact(ball.centerx, ball.centery)
            trigger_shake(10, 10)
            hit_counter += 1
            if hit_counter >= 3:
                ball_vel_x += math.copysign(0.5, ball_vel_x)
                ball_vel_y += math.copysign(0.5, ball_vel_y)
                hit_counter = 0
            # Move ball out of paddle to prevent sticking
            ball.right = paddle_ai.left

        # c) Ball goes out of bounds (scoring)
        if ball.left <= 0:
            # Player 2 scores
            score_player2 += 1
            # Reset ball to center
            ball.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            ball_vel_x *= -1 # Start moving towards the other player
        elif ball.right >= WINDOW_WIDTH:
            # Player 1 scores
            score_player1 += 1
            # Reset ball to center
            ball.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            ball_vel_x *= -1 # Start moving towards the other player


        # 12. Drawing everything
        # a) Create a temporary surface to draw on
        temp_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        temp_surface.fill(DARK_BLUE)
        
        # b) Draw the starfield
        for star in stars:
            star.update()
            star.draw(temp_surface)
            
        # c) Draw the particles
        for particle in particles[:]:
            particle.update()
            if particle.is_alive():
                particle.draw(temp_surface)
            else:
                particles.remove(particle)

        # d) Draw the paddles and the ball
        pygame.draw.rect(temp_surface, (255, 0, 0), paddle_player) # Red
        pygame.draw.rect(temp_surface, (0, 0, 255), paddle_ai) # Blue
        pygame.draw.ellipse(temp_surface, (255, 255, 255), ball) # White

        # e) Draw the middle line
        pygame.draw.aaline(temp_surface, YELLOW, (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT))

        # f) Draw the score labels
        player1_label = small_font.render("Player 1", True, YELLOW)
        temp_surface.blit(player1_label, (WINDOW_WIDTH / 4 - player1_label.get_width() / 2, 10))
        
        player2_label = small_font.render("Player 2", True, YELLOW)
        temp_surface.blit(player2_label, (WINDOW_WIDTH * 3 / 4 - player2_label.get_width() / 2, 10))

        # g) Draw the scores
        score_player1_text = font.render(str(score_player1), True, YELLOW)
        temp_surface.blit(score_player1_text, (WINDOW_WIDTH / 4 - score_player1_text.get_width() / 2, 40))

        score_player2_text = font.render(str(score_player2), True, YELLOW)
        temp_surface.blit(score_player2_text, (WINDOW_WIDTH * 3 / 4 - score_player2_text.get_width() / 2, 40))

        # 13. Update the display
        if shake_duration > 0:
            shake_offset_x = random.randint(-shake_intensity, shake_intensity)
            shake_offset_y = random.randint(-shake_intensity, shake_intensity)
            screen.blit(temp_surface, (shake_offset_x, shake_offset_y))
            shake_duration -= 1
        else:
            screen.blit(temp_surface, (0, 0))
        
        pygame.display.flip()

        # 14. Cap the frame rate
        clock.tick(60) # Run at 60 frames per second

    # --- End of Game ---
    pygame.quit()
    sys.exit()

# --- Run the game ---
if __name__ == "__main__":
    game()
