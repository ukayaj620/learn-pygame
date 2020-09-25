import pygame
from paddle import Paddle

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")

paddleA = Paddle(WHITE)
paddleA.rect.x = 50
paddleA.rect.y = 200

paddleB = Paddle(WHITE)
paddleB.rect.x = 750
paddleB.rect.y = 200

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

running = True

clock = pygame.time.Clock()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    all_sprites_list.update()

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [400, 0], [400, 500], 5)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
