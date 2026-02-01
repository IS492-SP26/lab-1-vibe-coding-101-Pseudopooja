import pygame
import sys

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

# --- Main Game Setup ---
def game():
    """
    Main function to initialize and run the Pong game.
    """
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
    score_player = 0
    score_ai = 0
    font = pygame.font.Font(None, 74) # Font for displaying score
    small_font = pygame.font.Font(None, 36) # Font for labels

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
        # Player paddle (W for up, S for down)
        if keys[pygame.K_w] and paddle_player.top > 0:
            paddle_player.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_player.bottom < WINDOW_HEIGHT:
            paddle_player.y += PADDLE_SPEED

        # 9. AI Paddle Movement
        # Simple AI: move the paddle's center towards the ball's center
        if paddle_ai.centery < ball.centery and paddle_ai.bottom < WINDOW_HEIGHT:
            paddle_ai.y += AI_PADDLE_SPEED
        if paddle_ai.centery > ball.centery and paddle_ai.top > 0:
            paddle_ai.y -= AI_PADDLE_SPEED

        # 10. Ball Movement
        ball.x += ball_vel_x
        ball.y += ball_vel_y

        # 11. Ball Collision Detection
        # a) Collision with top/bottom walls
        if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
            ball_vel_y *= -1 # Reverse vertical direction

        # b) Collision with paddles
        if ball.colliderect(paddle_player) or ball.colliderect(paddle_ai):
            ball_vel_x *= -1 # Reverse horizontal direction

        # c) Ball goes out of bounds (scoring)
        if ball.left <= 0:
            # AI scores
            score_ai += 1
            # Reset ball to center
            ball.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            ball_vel_x *= -1 # Start moving towards the other player
        elif ball.right >= WINDOW_WIDTH:
            # Player scores
            score_player += 1
            # Reset ball to center
            ball.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            ball_vel_x *= -1 # Start moving towards the other player


        # 12. Drawing everything
        # a) Clear the screen with the new background color
        screen.fill(DARK_BLUE)

        # b) Draw the paddles and the ball
        pygame.draw.rect(screen, YELLOW, paddle_player)
        pygame.draw.rect(screen, YELLOW, paddle_ai)
        pygame.draw.ellipse(screen, YELLOW, ball)

        # c) Draw the middle line
        pygame.draw.aaline(screen, YELLOW, (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT))

        # d) Draw the score labels
        player_label = small_font.render("Player", True, YELLOW)
        screen.blit(player_label, (WINDOW_WIDTH / 4 - player_label.get_width() / 2, 10))
        
        ai_label = small_font.render("AI", True, YELLOW)
        screen.blit(ai_label, (WINDOW_WIDTH * 3 / 4 - ai_label.get_width() / 2, 10))

        # e) Draw the scores
        score_player_text = font.render(str(score_player), True, YELLOW)
        screen.blit(score_player_text, (WINDOW_WIDTH / 4 - score_player_text.get_width() / 2, 40))

        score_ai_text = font.render(str(score_ai), True, YELLOW)
        screen.blit(score_ai_text, (WINDOW_WIDTH * 3 / 4 - score_ai_text.get_width() / 2, 40))


        # 13. Update the display
        pygame.display.flip()

        # 14. Cap the frame rate
        clock.tick(60) # Run at 60 frames per second

    # --- End of Game ---
    pygame.quit()
    sys.exit()

# --- Run the game ---
if __name__ == "__main__":
    game()
