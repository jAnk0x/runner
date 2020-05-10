import pygame
import sys
from variables import window_width, window_height, g, ground_level
import variables
from player import Player
from obstacle import Obstacle
from props import Prop, Ground, Background
from button import Button
from inputbox import InputBox
from result import Result
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
LARGE_FONT = pygame.font.SysFont(None, 115)
SMALL_FONT = pygame.font.SysFont(None, 40)


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()


player = Player()
player.rect.x = 400
player.rect.bottom = ground_level

props = []
backgound = Background(4)
ground = Ground()
props.append(backgound)
props.append(ground)

obstacle_width = 20
obstacle_height = 680
obstacle_gap = 150
obstacle = Obstacle(obstacle_width, obstacle_height, obstacle_gap)


def update_score():
    score_message = "Score: " + str(variables.score)
    score_text = SMALL_FONT.render(score_message, True, PURPLE)
    score_rect = score_text.get_rect()
    window.blit(score_text, score_rect)


def reset_game():
    player.reset()
    obstacle.reset()
    variables.score = 0


def game_menu(onClick=False):
    menu = True

    window.fill(pygame.Color(225, 225, 225))
    large_text = LARGE_FONT.render("Runner", True, PURPLE)
    text_rect = large_text.get_rect()
    text_rect.center = (window_width // 2, window_height // 2)
    window.blit(large_text, text_rect)

    start_button = Button("Go!", window_width // 2 - 250,
                          window_height // 2 + 100, 100, 200, PURPLE, GREEN, BLACK, 40)
    scores_button = Button("High Scores", window_width // 2 + 50,
                           window_height // 2 + 100, 100, 200, PURPLE, GREEN, BLACK, 40)

    while menu:
        mouse_clicks = pygame.mouse.get_pressed()
        if onClick and mouse_clicks[0] == 0:
            onClick = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_game(True)

        mouse_pos = pygame.mouse.get_pos()

        start_button.draw(mouse_pos, window)
        scores_button.draw(mouse_pos, window)
        if not onClick and start_button.is_clicked(mouse_pos, mouse_clicks):
            main_game()
        elif not onClick and scores_button.is_clicked(mouse_pos, mouse_clicks):
            scoreboard()
        pygame.display.update()

        clock.tick(15)


def update_scoreboard(score_list, name):
    result = Result(variables.score, name)
    if len(score_list) < 5:
        score_list.append(result)
        score_list.sort(key=lambda x: x.score, reverse=True)
    elif score_list[4].score < variables.score:
        score_list[4] = result

    S = "\n".join([str(s) for s in score_list])
    with open('highscores.txt', 'w') as high_scores:
        high_scores.write(S)


def get_scoreboard():
    with open('highscores.txt', 'r') as high_scores:
        scoreboard = [line.rstrip() for line in high_scores]
        score_list = [Result.parse(score) for score in scoreboard]
        score_list.sort(key=lambda x: x.score, reverse=True)
        return score_list


def is_good_run(score_list):
    if variables.score == 0 or (len(score_list) > 5 and score_list[-1].score >= variables.score):
        return False
    return True


def game_over():
    score_list = get_scoreboard()
    good_run = is_good_run(score_list)

    large_text = LARGE_FONT.render("Game Over", True, PURPLE)
    text_rect = large_text.get_rect()
    text_rect.center = (window_width // 2, window_height // 2 - 100)
    window.blit(large_text, text_rect)

    restart_button = Button("Restart", window_width //
                            2 + 50, 500, 100, 200, PURPLE, GREEN, BLACK, 40)
    menu_button = Button("Main Menu", window_width //
                         2 - 250, 500, 100, 200, PURPLE, GREEN, BLACK, 40)

    if good_run:
        input_box = InputBox(window_width // 2, 420, 130, 30)
        text = None

        name_text = SMALL_FONT.render("Enter your name: ", True, PURPLE)
        text_rect = name_text.get_rect()
        text_rect.center = (window_width // 2, window_height // 2)
        window.blit(name_text, text_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                text = input_box.handle_event(event)
            if text:
                update_scoreboard(score_list, text)

            input_box.draw(window)

            mouse_pos = pygame.mouse.get_pos()
            mouse_clicks = pygame.mouse.get_pressed()
            restart_button.draw(mouse_pos, window)
            menu_button.draw(mouse_pos, window)

            if restart_button.is_clicked(mouse_pos, mouse_clicks):
                main_game()
            elif menu_button.is_clicked(mouse_pos, mouse_clicks):
                game_menu(True)

            pygame.display.update()
            clock.tick(15)
    else:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse_pos = pygame.mouse.get_pos()
            mouse_clicks = pygame.mouse.get_pressed()
            restart_button.draw(mouse_pos, window)
            menu_button.draw(mouse_pos, window)

            if restart_button.is_clicked(mouse_pos, mouse_clicks):
                main_game()
            elif menu_button.is_clicked(mouse_pos, mouse_clicks):
                game_menu(True)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                main_game()

            pygame.display.update()
            clock.tick(15)


def update_all():
    for prop in props:
        if not isinstance(prop, Ground):
            prop.draw(window)
            prop.update()

    player.draw(window)
    obstacle.draw(window)
    ground.draw(window)
    ground.update()
    player.update()
    obstacle.update()

    update_score()


def pause():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(100)
                return


def scoreboard():
    high_scores = get_scoreboard()

    window.fill(pygame.Color(225, 225, 225))

    large_text = LARGE_FONT.render("Scoreboard", True, BLACK)
    text_rect = large_text.get_rect()
    text_rect.center = (window_width // 2, 100)
    window.blit(large_text, text_rect)

    score_font = pygame.font.SysFont(None, 70)
    for i, result in enumerate(high_scores):
        score_text = score_font.render(
            str(i + 1) + '. ' + result.name + " " + str(result.score), True, RED)
        text_rect = score_text.get_rect()
        text_rect.centery = 200 + i * 100
        text_rect.left = window_width // 2 - 100
        window.blit(score_text, text_rect)

    back_button = Button("Back", 20,
                         600, 100, 200, PURPLE, GREEN, BLACK, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicks = pygame.mouse.get_pressed()
        back_button.draw(mouse_pos, window)
        if back_button.is_clicked(mouse_pos, mouse_clicks):
            game_menu()

        pygame.display.flip()


def main_game(onSpace=False):
    reset_game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if onSpace and not keys[pygame.K_SPACE]:
            onSpace = False

        window.fill(pygame.Color(225, 225, 225))
        update_all()

        # pygame.draw.rect(window, RED, player.rect)

        if player.check_collision(obstacle):
            game_over()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w] or (not onSpace and keys[pygame.K_SPACE]):
            player.jump()
        if keys[pygame.K_ESCAPE]:
            pause()
        pygame.display.flip()
        clock.tick(60)


game_menu()
main_game()
