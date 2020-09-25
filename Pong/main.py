import pygame
from Pong.paddle import Paddle
from Pong.ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = {
    "width": 800,
    "height": 500
}
screen = pygame.display.set_mode((size["width"], size["height"]))
pygame.display.set_caption("Pong Game")

paddleA = Paddle(WHITE, size)
paddleA.rect.x = 25
paddleA.rect.y = 200

paddleB = Paddle(WHITE, size)
paddleB.rect.x = 750
paddleB.rect.y = 200

ball = Ball(WHITE, size)
ball.rect.x = size["width"] // 2 - 12
ball.rect.y = size["height"] // 2

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

running = True

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up()
    if keys[pygame.K_s]:
        paddleA.move_down()
    if keys[pygame.K_UP]:
        paddleB.move_up()
    if keys[pygame.K_DOWN]:
        paddleB.move_down()

    all_sprites_list.update()

    if ball.rect.x >= size["width"] - 25:
        scoreA += 1
        ball.velocityX = -ball.velocityX

    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocityX = -ball.velocityX

    if ball.rect.y > size["height"] - 25:
        ball.velocityY = -ball.velocityY

    if ball.rect.y < 0:
        ball.velocityY = -ball.velocityY

        # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_rect(ball, paddleA) or pygame.sprite.collide_rect(ball, paddleB):
        ball.bounce()

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [400, 0], [400, 500], 5)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 72)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (size["width"] // 4 * 1, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (size["width"] // 4 * 3, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
