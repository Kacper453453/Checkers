import pygame as pg
from constants import SQUARE_SIZE

class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, color, x, y):
        self.color = color
        self.radius = SQUARE_SIZE//2 - self.PADDING
        self.x = x
        self.y = y

    def draw(self, surface):
        pg.draw.circle(surface, self.color,
                       (self.x*SQUARE_SIZE+self.PADDING, self.y*SQUARE_SIZE+self.PADDING),
                       self.radius + self.OUTLINE)
