import pygame
import math
from variables import g, ground_level
RED = (200, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sheet = pygame.image.load("run.png")
        self.frames = []
        self.create_frames()

        self.image = self.frames[0]
        self.frame = 0
        self.rect = self.image.get_rect()

        self.velocityY = 0
        self.flying = False

    def create_frames(self):
        sheet_rect = self.sheet.get_rect()
        w = sheet_rect.width
        dx = w // 8

        for i in range(0, w, dx):
            location = (i + 62, 62)
            self.frames.append(self.sheet.subsurface(
                pygame.Rect(location, (26, 38))))

    def next_frame(self):
        if self.frame == 7:
            self.frame = -1
        self.frame += 0.5
        self.image = self.frames[math.trunc(self.frame)]

    def jump(self):
        if not self.flying:
            self.velocityY = 22
            self.flying = True

    def check_collision(self, sprite):
        return pygame.sprite.collide_rect(self, sprite)

    def update(self):
        self.rect.bottom -= self.velocityY
        if self.rect.bottom >= ground_level:
            self.rect.bottom = ground_level
            self.velocityY = 0
            self.next_frame()
            self.flying = False
        elif self.rect.y < ground_level:
            self.velocityY += g
