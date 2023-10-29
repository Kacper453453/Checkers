import pygame as pg
from piece import Piece
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROWS, COLS



class Board:
    COLOR1 = (255, 255, 255)
    COLOR2 = (0, 0, 0)
    def __init__(self):
        self.board_surface = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = []
        self.pieces = []
    def draw_squares(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if row % 2 == 0 and col % 2 == 0:
                    pg.draw.rect(surface, self.COLOR1, (row*))
                else:
                    pg.draw.rect(surface, self.COLOR2, )


    def draw(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                pass



                # pg.draw.rect(self.board, (210, 180, 140),
                #              (x*RECT_WIDTH, y*RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
                # pg.draw.rect(self.board, (210, 180, 140),
                #              ((x + 1) * RECT_WIDTH, (y + 1) * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))

    def display(self, screen):
        screen.blit(self.board, (0, 0))

    def set_up_pieces(self):
        for i in range(8):
            self.pieces.append(Piece("black", i, 1))
            self.pieces.append(Piece("white", i, 6))

    def draw_pieces(self, surface):
        for piece in self.pieces:
            piece.draw(surface)