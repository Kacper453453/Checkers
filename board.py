import pygame as pg
from piece import Piece
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROWS, COLS, SQUARE_SIZE, WHITE, BROWN, LIGHT_GREEN


class Board:
    COLOR1 = (0, 0, 0)
    COLOR2 = (240, 190, 130)
    def __init__(self):
        self.board_surface = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = []
        self.pieces = []
        self.selected = None
    def draw(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if self.selected:
                        if (row, col) == self.selected:
                            pg.draw.rect(surface, LIGHT_GREEN,
                                         (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        else:
                            pg.draw.rect(surface, self.COLOR1,
                                         (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    else:
                        pg.draw.rect(surface, self.COLOR1,
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                else:
                    pg.draw.rect(surface, self.COLOR2,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def set_up_pieces(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(WHITE, row, col))
                    elif row > 4:
                        self.board[row].append(Piece(BROWN, row, col))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    piece = self.board[row][col]
                    piece.draw(surface)



