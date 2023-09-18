import pygame
import consts
import random

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("THE FLAG")


def draw_game():
    screen.fill(consts.GREEN)
    grass = pygame.transform.scale(consts.GRASS, (50, 50))
    for i in range(20):
        x = random.randint(0, 950)
        y = random.randint(0, 450)
        screen.blit(grass, (x, y))
    # flag = pygame.transform.scale(consts.FLAG, (40, 60))
    # screen.blit(flag, (21 * 20, 46 * 20))
    pygame.display.flip()


def flag_place():
    # flag = pygame.transform.scale(consts.FLAG, (40, 60))
    screen.blit(consts.FLAG, (21*20, 46*20))
    pygame.display.flip()
