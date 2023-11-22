import pygame as pg

# game settings
SCREEN_WIDTH =  800

BOARD_SIZE = SCREEN_WIDTH - 200
SCREEN_HEIGHT = BOARD_SIZE
ROWS, COLS = 8, 8
SQUARE_SIZE = BOARD_SIZE // ROWS
RECT_WIDTH, RECT_HEIGHT = SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8

#img
CROWN = pg.transform.scale(pg.image.load('crown.png'), (44, 25))


#rgb
WHITE = (255, 255, 255)
COLOR_UP = (255, 255, 255)
COLOR_DOWN = (186, 101, 32) #Brown
LIGHT_BROWN = (240, 190, 130)
BLACK = (0, 0, 0)
GRAY = (222, 222, 222)
LIGHT_GREEN = (201, 250, 170)






