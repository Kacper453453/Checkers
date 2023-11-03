import pygame as pg
from piece import Piece
from constants import ROWS, COLS, SQUARE_SIZE, LIGHT_GREEN, BLACK, LIGHT_BROWN, BOARD_SIZE



class Board:
    def __init__(self):
        self.board_surface = pg.Surface([BOARD_SIZE, BOARD_SIZE])
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
            board_row = []
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        board_row.append(Piece(row, col, True))
                    elif row > 4:
                        board_row.append(Piece(row, col, False))
                    else:
                        board_row.append(0)
                else:
                    board_row.append(0)

            self.board.append(board_row)

    def draw_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    piece = self.board[row][col]
                    piece.draw(surface)



