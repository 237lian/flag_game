import pygame
import consts
import screen


def create():
    grid = []
    for i in range(25):
        row = []
        for j in range(50):
            row.append("empty")
        grid.append(row)
    return grid


def draw_grid():
    block_size = 20
    screen.screen.fill(consts.BLACK)
    for x in range(consts.WINDOW_WIDTH):
        for y in range(consts.WINDOW_HEIGHT):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen.screen, consts.GREEN, rect, 1)
    pygame.display.flip()

