
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- PLAYER INPUT ----
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s]:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP]:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_paddle.y += paddle_speed

    # Keep paddles on screen
    left_paddle.y = max(0, min(left_paddle.y, HEIGHT - paddle_height))
    right_paddle.y = max(0, min(right_paddle.y, HEIGHT - paddle_height))

    # ---- BALL MOVEMENT ----
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # ---- SCORING ----
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
    if ball.right >= WIDTH:
        left_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)

    # ---- DRAW OBJECTS ----
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = font.render(f"{left_score}   {right_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 30, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()

