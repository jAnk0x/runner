import pygame
import sys
from variables import window_width, window_height, g, ground_level
import variables
from player import Player
from obstacle import Obstacle
from props import Prop, Ground, Background
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()


sprites = pygame.sprite.Group()
player = Player()
player.rect.x = 400
player.rect.bottom = ground_level
sprites.add(player)

props = []
ground = Ground()
backgound = Background(4)
props.append(backgound)
props.append(ground)

obstacle = Obstacle(20, 100)
sprites.add(obstacle)


def update_score():
    score_message = "Score: " + str(variables.score)
    score_font = pygame.font.SysFont(None, 40)
    score_text = score_font.render(score_message, True, PURPLE)
    score_rect = score_text.get_rect()
    window.blit(score_text, score_rect)


def reset_objects():
    player.rect.bottom = ground_level
    obstacle.rect.left = window_width


def game_over():
    large_font = pygame.font.SysFont(None, 115)
    large_text = large_font.render("Game Over", True, PURPLE)
    text_rect = large_text.get_rect()
    text_rect.center = (window_width // 2, window_height // 2)
    window.blit(large_text, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            main_game()

        pygame.display.update()
        clock.tick(15)


def main_game():
    reset_objects()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(pygame.Color(225, 225, 225))

        for prop in props:
            prop.draw(window)
            prop.update()

        update_score()

        # pygame.draw.rect(window, RED, player.rect)
        sprites.update()
        # if player.check_collision(obstacle):
        #    game_over()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.jump()

        sprites.draw(window)

        pygame.display.flip()
        clock.tick(60)
        # pygame.time.delay(5)


main_game()
