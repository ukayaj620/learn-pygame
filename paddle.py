import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):

        super(Paddle, self).__init__()
        self.width = 25
        self.height = 100

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))

        pygame.draw.rect(self.image, color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

        self.speed = 8

