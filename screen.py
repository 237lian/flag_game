import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("THE FLAG")


def draw_game():
    screen.fill(consts.GREEN)
    pygame.display.update()


while True:
    pass
