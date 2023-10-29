import pygame as pg

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
RECT_WIDTH, RECT_HEIGHT = SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8

class Board:
    def __init__(self):
        self.board = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        for x in range(0, 8, 2):
            for y in range(0, 8, 2):
                pg.draw.rect(self.board, (210, 180, 140),
                             (x*RECT_WIDTH, y*RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
                pg.draw.rect(self.board, (210, 180, 140),
                             ((x + 1) * RECT_WIDTH, (y + 1) * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))

    def display(self, screen):
        screen.blit(self.board, (0, 0))