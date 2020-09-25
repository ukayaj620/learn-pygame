import pygame
from random import randint


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, screen_size):
        super(Ball, self).__init__()
        self.radius = 25
        self.screen_size = screen_size

        self.image = pygame.Surface([self.radius, self.radius])
        self.image.fill((255, 255, 255))

        pygame.draw.rect(self.image, color, [0, 0, self.radius, self.radius])

        self.rect = self.image.get_rect()
        self.velocityX = randint(2, 5)
        self.velocityY = randint(-5, 5)

    def update(self):
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

    def bounce(self):
        self.velocityX = -self.velocityX
        self.velocityY = randint(-5, 5)
