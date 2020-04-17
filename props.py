import pygame
from variables import ground_level, window_width, game_speed


class Prop():
    def __init__(self, img, speed=game_speed, top=0):
        self.image = img
        self.rect1 = self.image.get_rect()
        self.rect1.top = top

        self.rect2 = self.rect1.copy()
        self.rect2.left = window_width

        self.speed = speed

    def update(self):
        self.rect1.right -= self.speed
        self.rect2.right -= self.speed
        if self.rect1.right <= 0:
            self.rect1.left = self.rect2.right
        elif self.rect2.right <= 0:
            self.rect2.left = self.rect1.right

    def draw(self, window):
        window.blit(self.image, self.rect1)
        window.blit(self.image, self.rect2)


class Ground(Prop):
    def __init__(self):
        self.image = pygame.image.load(
            "grass-bg.png").convert_alpha()
        super().__init__(self.image, game_speed, ground_level)


class Background(Prop):
    def __init__(self, speed, top=0):
        self.image = pygame.image.load("mountains.png").convert_alpha()
        super().__init__(self.image, speed, top)
