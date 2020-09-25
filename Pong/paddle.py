import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, screen_size):

        super(Paddle, self).__init__()
        self.width = 25
        self.height = 100

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))

        pygame.draw.rect(self.image, color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

        self.screen_size = screen_size

        self.speed = 10

    def __check_boundaries(self):
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > (self.screen_size["height"] - self.height):
            self.rect.y = (self.screen_size["height"] - self.height)

    def move_up(self):
        self.rect.y -= self.speed
        self.__check_boundaries()

    def move_down(self):
        self.rect.y += self.speed
        self.__check_boundaries()
