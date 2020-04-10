import pygame
GRASS = (0, 150, 0)


class Ground(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GRASS)
        #self.image = pygame.image.load("grass.png")

        self.rect = self.image.get_rect()
        self.rect.bottom = 720
