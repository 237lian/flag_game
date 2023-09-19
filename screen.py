import pygame
import consts
import random
import game_field
import main

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("THE FLAG")


def choose_random():
    plant_list = []
    for i in range(20):
        x = random.randint(0, 950)
        y = random.randint(0, 450)
        plant_list.append((x, y))
    return plant_list


list_of_plants = choose_random()


def draw_game():
    screen.fill(consts.GREEN)
    grass = pygame.transform.scale(consts.GRASS, (50, 50))
    for plant in list_of_plants:
        screen.blit(grass, (plant[0], plant[1]))
    game_field.flag_place()
    pygame.display.flip()


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_starting_message():
    draw_message(consts.STARTING_MESSAGE, consts.MESSAGE_SIZE,
                 consts.MESSAGE_COLOR, consts.MESSAGE_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
