import pygame as pg
from board import Board
from constants import SQUARE_SIZE


pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
RECT_WIDTH, RECT_HEIGHT = SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8


class GameManager:
    def __init__(self):
        pg.display.set_caption('Checkers')
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

        self.board = Board()
        self.board.set_up_pieces()

    def loop(self):
        self.board.draw(self.screen)
        self.board.draw_pieces(self.screen)

        pg.display.flip()
        self.clock.tick(60)

    def handle_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            pos  = pg.mouse.get_pos()

            row = (pos[1] // SQUARE_SIZE)
            col = (pos[0] // SQUARE_SIZE)



            self.board.selected = (row, col)
            print(self.board.selected)


def main():
    gm = GameManager()

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            gm.handle_click(event)


        gm.loop()


if __name__ == "__main__":
    main()

