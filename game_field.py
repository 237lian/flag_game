import pygame
import consts
import screen
import random
import soldier


def enter_flag_in_matrix(row, col):
    return 21 <= row <= 24 and 47 <= col <= 49


def soldier_body_start_place_in_matrix(row, col):
    return 0 <= row <= 2 and 0 <= col <= 1


def soldier_legs_start_place_in_matrix(row, col):
    return row == 3 and 0 <= col <= 1


def create_mine():
    list_to_return = []
    used = []
    for i in range(20):
        row = random.randint(0, 24)
        col = random.randint(0, 47)
        while enter_flag_in_matrix(row, col) or soldier_body_start_place_in_matrix(row, col) or \
                soldier_legs_start_place_in_matrix(row, col) or (row, col) in used:
            row = random.randint(0, 24)
            col = random.randint(0, 47)
        used.append((row, col))
        used.append((row, col + 1))
        used.append((row, col + 2))
        list_to_return.append((row, col))
    return list_to_return


list_of_mines = create_mine()


def add_mine_to_matrix(list_to_use, matrix):
    for bomb in list_to_use:
        row = int(bomb[0])
        col = int(bomb[1])
        for i in range(3):
            matrix[row][col] = consts.MINE
            col += 1
    return matrix


def create():
    grid = []
    for i in range(consts.MATRIX_ROWS):
        row = []
        for j in range(consts.MATRIX_COLS):
            if enter_flag_in_matrix(i, j):
                row.append(consts.FLAG)
            elif soldier_body_start_place_in_matrix(i, j):
                row.append(consts.BODY)
            elif soldier_legs_start_place_in_matrix(i, j):
                row.append(consts.LEGS)
            else:
                row.append(consts.NOTHING)
        grid.append(row)
    return grid


grid = create()
new_grid = add_mine_to_matrix(list_of_mines, grid)


def draw_mine_to_grid(list_to_use):
    mine = pygame.transform.scale(consts.MINE_PHOTO, (60, 20))
    for bomb in list_to_use:
        x = int(bomb[1]) * 20
        y = int(bomb[0]) * 20
        screen.screen.blit(mine, (x, y))


def draw_grid():
    block_size = 20
    screen.screen.fill(consts.BLACK)
    for x in range(consts.WINDOW_WIDTH):
        for y in range(consts.WINDOW_HEIGHT):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen.screen, consts.GREEN, rect, 1)
    draw_mine_to_grid(list_of_mines)
    soldier_night = pygame.transform.scale(consts.SOLDIER_NIGHT, (40, 80))
    screen.screen.blit(soldier_night, (soldier.soldier_x, soldier.soldier_y))
    pygame.display.flip()
    pygame.time.wait(1000)


def flag_place():
    flag = pygame.transform.scale(consts.FLAG_PHOTO, (60, 80))
    screen.screen.blit(flag, (940, 420))
    pygame.display.flip()

