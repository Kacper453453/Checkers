import pygame as pg
from piece import Piece
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROWS, COLS, SQUARE_SIZE


class Board:
    COLOR1 = (0, 0, 0)
    COLOR2 = (240, 190, 130)
    def __init__(self):
        self.board_surface = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = []
        self.pieces = []
    def draw(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    pg.draw.rect(surface, self.COLOR1,
                                 (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pg.draw.rect(surface, self.COLOR2,
                                 (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def set_up_pieces(self):
        pass
