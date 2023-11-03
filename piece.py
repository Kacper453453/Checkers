import pygame as pg
from constants import SQUARE_SIZE, COLOR_UP, COLOR_DOWN, GRAY


class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, row, col, up):
        self.up = up
        self.radius = SQUARE_SIZE//2 - self.PADDING
        self.row = row
        self.col = col

        self.pos = (SQUARE_SIZE * self.col + SQUARE_SIZE // 2,
                    SQUARE_SIZE * self.row + SQUARE_SIZE // 2)
        self.color = COLOR_UP if up else COLOR_DOWN

    def draw(self, surface):
        pg.draw.circle(surface, self.color, (self.pos[0], self.pos[1]), self.radius + self.OUTLINE)
        pg.draw.circle(surface, GRAY, (self.pos[0], self.pos[1]),
                       self.radius, self.OUTLINE, True)





