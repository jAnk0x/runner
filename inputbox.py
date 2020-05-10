import pygame

PURPLE = (255, 0, 255)
GREEN = (20, 255, 140)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = (x, y)
        self.color = PURPLE
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) <= 10:
                self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
