import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

MATRIX_ROWS = 25
MATRIX_COLS = 50

GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRASS = pygame.image.load('grass.png')
FLAG_PHOTO = pygame.image.load('flag.png')
EXPLOSION = pygame.image.load('explotion.png')
MINE_PHOTO = pygame.image.load('mine.png')
SOLDIER = pygame.image.load('soldier.png')
SNAKE = pygame.image.load('snake.png')
SOLDIER_NIGHT = pygame.image.load('soldier_nigth.png')
INJURY = pygame.image.load('injury.png')
SOLDIER_2 = pygame.image.load('soldier (2).png')

NOTHING = "empty"
FLAG = "flag"
LEGS = "legs"
BODY = "body"
MINE = "mine"

FONT_NAME = "Calibri"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

STARTING_MESSAGE = "Welcome to The Flag game. Have Fun!"
MESSAGE_COLOR = WHITE
MESSAGE_SIZE = 30
MESSAGE_LOCATION = (40, 0)
