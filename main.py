import pygame
import screen
import consts

state = {
    "is_window_open": True
}


def main():
    pygame.init()
    while state["is_window_open"]:
        handle_user_events()
        screen.draw_game()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False


main()
