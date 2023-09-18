import pygame
import screen
import game_field
import time
import sys
import consts

state = {
    "is_window_open": True
}


def main():
    pygame.init()
    screen.draw_game()
    while state["is_window_open"]:
        screen.flag_place()
        # game_field.draw_grid()
        handle_user_events()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_field.draw_grid()
                # pygame.time.wait(1000)


main()
