# Create a simple 2-player Pong game using pygame.
# Requirements:
# - Window size 800x500
# - Left paddle: W/S keys
# - Right paddle: Up/Down arrow keys
# - Ball moves and bounces off paddles and walls
# - Score increases when ball passes a paddle
# - Display score on screen
# - Keep the code simple and readable


import pygame
import sys
import random
import math
pygame.init()
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (10, 20, 40)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
FPS = 60
FONT = pygame.font.SysFont("comicsans", 40)

# Create starfield
class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.brightness = random.randint(100, 255)
        self.twinkle_speed = random.uniform(0.05, 0.2)
        self.twinkle_phase = random.uniform(0, 6.28)

    def update(self):
        self.twinkle_phase += self.twinkle_speed
        self.brightness = int(150 + 105 * ((1 + math.sin(self.twinkle_phase)) / 2))

    def draw(self, win):
        color = (self.brightness, self.brightness, self.brightness * 0.8)
        pygame.draw.circle(win, color, (int(self.x), int(self.y)), 1)

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

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 7

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        elif not up and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.x_vel = random.choice([-5, 5])
        self.y_vel = random.choice([-5, 5])

    def move(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def draw(self, win):
        pygame.draw.ellipse(win, WHITE, self.rect)

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.x_vel *= -1
        self.y_vel = random.choice([-5, 5])

def create_impact(x, y, num_particles=15):
    for _ in range(num_particles):
        particles.append(Particle(x, y))

def draw(win, paddles, ball, scores):
    win.fill(DARK_BLUE)
    # Draw twinkling stars
    for star in stars:
        star.update()
        star.draw(win)
    
    # Update and draw particles
    for particle in particles[:]:
        particle.update()
        if particle.is_alive():
            particle.draw(win)
        else:
            particles.remove(particle)
    
    for paddle in paddles:
        paddle.draw(win)
    ball.draw(win)
    score_text = FONT.render(f"{scores[0]} - {scores[1]}", 1, WHITE)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.update()

def main():
    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2)
    paddles = [left_paddle, right_paddle]
    scores = [0, 0]
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move(up=True)
        if keys[pygame.K_s]:
            left_paddle.move(up=False)
        if keys[pygame.K_UP]:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN]:
            right_paddle.move(up=False)
        ball.move()
        if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
            ball.y_vel *= -1
        
        # Check paddle collisions and create impact
        if ball.rect.colliderect(left_paddle.rect):
            ball.x_vel *= -1
            create_impact(ball.rect.centerx, ball.rect.centery)
        if ball.rect.colliderect(right_paddle.rect):
            ball.x_vel *= -1
            create_impact(ball.rect.centerx, ball.rect.centery)
        
        if ball.rect.left <= 0:
            scores[1] += 1
            ball.reset()
        if ball.rect.right >= WIDTH:
            scores[0] += 1
            ball.reset()
        draw(WIN, paddles, ball, scores)
    pygame.quit()

if __name__ == "__main__":
    main()
