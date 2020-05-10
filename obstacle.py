import pygame
import variables
import random

YELLOW = (255, 255, 102)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, gap):
        super().__init__()

        self.width = width
        self.height = height
        self.gap = gap

        self.image = pygame.Surface([width, variables.window_height])
        self.image.fill(YELLOW)

        self.rect_b = self.image.get_rect()
        self.rect_b.top = variables.window_height - \
            random.randrange(20, self.height)
        self.rect_b.left = variables.window_width

        self.rect_t = self.image.get_rect()
        self.rect_t.bottom = self.rect_b.top - self.gap
        #2 * self.height - \
        #    (variables.window_height - self.rect_b.top)
        self.rect_t.left = variables.window_width

        self.rects = []
        self.rects.append(self.rect_b)
        self.rects.append(self.rect_t)

    def update(self):
        self.rect_b.left -= variables.game_speed
        self.rect_t.left -= variables.game_speed
        if self.rect_b.right < 0:
            self.rect_b.top = variables.window_height - \
                random.randrange(20, self.height)
            self.rect_b.left = variables.window_width

            self.rect_t.bottom = self.rect_b.top - self.gap
            self.rect_t.left = variables.window_width
            variables.score += 1

    def reset(self):
        self.rect_b.top = variables.window_height - \
            random.randrange(20, self.height)
        self.rect_b.left = variables.window_width

        self.rect_t = self.image.get_rect()        
        self.rect_t.bottom = self.rect_b.top - self.gap
        self.rect_t.left = variables.window_width

        self.rects.clear()
        self.rects.append(self.rect_b)
        self.rects.append(self.rect_t)

    def draw(self, window):
        window.blit(self.image, self.rect_b)
        window.blit(self.image, self.rect_t)
