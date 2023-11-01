import pygame as pg
from piece import Piece
from constants import ROWS, COLS, SQUARE_SIZE, WHITE, BROWN, LIGHT_GREEN, BLACK, LIGHT_BROWN


class Board:
    def __init__(self):
        self.board = []
        self.selected = None
    def draw(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    pg.draw.rect(surface, BLACK,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                    # highlight selected square
                    if (row, col) == self.selected:
                        pg.draw.rect(surface, LIGHT_GREEN,
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pg.draw.rect(surface, LIGHT_BROWN,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_possible_moves(self, moves):
        pass

    def calculate_board_possition(self, x, y):
        row = (y // SQUARE_SIZE)
        col = (x // SQUARE_SIZE)
        return row, col


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



