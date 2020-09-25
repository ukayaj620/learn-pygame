import pygame
from random import randrange


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, screen_size):
        super(Ball, self).__init__()
        self.radius = 25
        self.screen_size = screen_size

        self.image = pygame.Surface([self.radius, self.radius])
        self.image.fill((255, 255, 255))

        pygame.draw.rect(self.image, color, [0, 0, self.radius, self.radius])

        self.rect = self.image.get_rect()

        self.epsilon = 0.80

        self.velocityX = randrange(2, 5)
        self.velocityY = randrange(-5, 5) + self.epsilon

    def update(self):
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

    def bounce(self):
        self.velocityX = -self.velocityX
        self.velocityY = self.velocityY
