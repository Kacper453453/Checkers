import pygame as pg
from constants import SQUARE_SIZE, COLOR_UP, COLOR_DOWN, GRAY, CROWN

class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, row, col, side):
        self.side = side
        self.radius = SQUARE_SIZE//2 - self.PADDING
        self.row = row
        self.col = col

        self.pos = (SQUARE_SIZE * self.col + SQUARE_SIZE // 2,
                    SQUARE_SIZE * self.row + SQUARE_SIZE // 2)
        self.color = COLOR_UP if self.side == 'up' else COLOR_DOWN
        self.king = False

    def compare(self, others):
        return any(isinstance(piece, Piece) for piece in others)

    def update_pos(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

        new_pos = (SQUARE_SIZE * new_col + SQUARE_SIZE // 2,
                    SQUARE_SIZE * new_row + SQUARE_SIZE // 2)

        self.pos = new_pos


    def draw(self, surface):
        pg.draw.circle(surface, self.color, (self.pos[0], self.pos[1]), self.radius + self.OUTLINE)
        pg.draw.circle(surface, GRAY, (self.pos[0], self.pos[1]),
                       self.radius, self.OUTLINE, True)
        if self.king:
            surface.blit(CROWN, (self.pos[0] - CROWN.get_width()//2, self.pos[1] - CROWN.get_height()//2))






