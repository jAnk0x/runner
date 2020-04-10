import pygame
import variables
YELLOW = (255, 255, 102)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(YELLOW)
        #self.image = pygame.image.load("grass.png")

        self.rect = self.image.get_rect()
        self.rect.bottom = variables.ground_level
        self.rect.left = variables.window_width

    def update(self):
        self.rect.left -= variables.game_speed
        if self.rect.right < 0:
            self.rect.left = variables.window_width
            variables.score += 1
