import pygame
import screen
import game_field
import time
import sys
import consts
import soldier

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE
}


def main():
    pygame.init()
    screen.draw_game()
    game_field.flag_place()
    while state["is_window_open"]:
        handle_user_events()
        pygame.display.flip()
        soldier.soldier_place()

        if touched_mine():
            screen.draw_lose_message()
            pygame.display.flip()
            pygame.time.wait(3000)
            state["is_window_open"] = False
        if touched_flag():
            screen.draw_win_message()
            pygame.display.flip()
            pygame.time.wait(3000)
            state["is_window_open"] = False

        screen.draw_game()
        pygame.display.flip()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_field.draw_grid()
            if event.key == pygame.K_DOWN:
                soldier.soldier_y = soldier.move_down(soldier.soldier_y)
            if event.key == pygame.K_UP:
                soldier.soldier_y = soldier.move_up(soldier.soldier_y)
            if event.key == pygame.K_RIGHT:
                soldier.soldier_x = soldier.move_right(soldier.soldier_x)
            if event.key == pygame.K_LEFT:
                soldier.soldier_x = soldier.move_left(soldier.soldier_x)


def touched_mine():
    soldier_legs = soldier.soldier_legs()
    for place in soldier_legs:
        col = place[0]
        row = place[1]
        if game_field.new_grid[row][col] == consts.MINE:
            return True
    return False


def touched_flag():
    soldier_body = soldier.soldier_body()
    for place in soldier_body:
        col = place[0]
        row = place[1]
        if game_field.new_grid[row][col] == consts.FLAG:
            return True
    return False


if __name__ == '__main__':
    main()
