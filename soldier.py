import pygame
import consts
import screen

# pixels
soldier_x = 0
soldier_y = 0


def pixel_to_index(num):
    return num // 20


def soldier_body():
    return [(pixel_to_index(soldier_x), pixel_to_index(soldier_y)),
            (pixel_to_index(soldier_x) + 1, pixel_to_index(soldier_y)),
            (pixel_to_index(soldier_x), pixel_to_index(soldier_y) + 1),
            (pixel_to_index(soldier_x) + 1, pixel_to_index(soldier_y) + 1),
            (pixel_to_index(soldier_x), pixel_to_index(soldier_y) + 2),
            (pixel_to_index(soldier_x) + 1, pixel_to_index(soldier_y) + 2)]


def soldier_legs():
    return [(pixel_to_index(soldier_x), pixel_to_index(soldier_y) + 3),
            (pixel_to_index(soldier_x) + 1, pixel_to_index(soldier_y) + 3)]


def soldier_place():
    soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
    screen.screen.blit(soldier, (soldier_x, soldier_y))
    pygame.display.flip()


def move_right(x):
    x += 20
    if x > 960:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (soldier_x, soldier_y))
        pygame.display.flip()
        return soldier_x
    else:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (x, soldier_y))
        pygame.display.flip()
        return x


def move_left(x):
    x -= 20
    if x < 0:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (soldier_x, soldier_y))
        pygame.display.flip()
        return soldier_x
    else:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (x, soldier_y))
        pygame.display.flip()
        return x


def move_up(y):
    y -= 20
    if y < 0:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (soldier_x, soldier_y))
        pygame.display.flip()
        return soldier_y
    else:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (soldier_x, y))
        pygame.display.flip()
        return y


def move_down(y):
    y += 20
    if y > 420:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (soldier_x, soldier_y))
        pygame.display.flip()
        return soldier_y
    else:
        soldier = pygame.transform.scale(consts.SOLDIER, (40, 80))
        screen.screen.blit(soldier, (soldier_x, y))
        pygame.display.flip()
        return y
