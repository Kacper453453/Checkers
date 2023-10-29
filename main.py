import pygame as pg
from board import Board


pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
RECT_WIDTH, RECT_HEIGHT = SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8


class GameManager:
    def __init__(self):
        pg.display.set_caption('Checkers')
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

    def loop(self):
        pg.display.flip()
        self.clock.tick(60)



def main():
    gm = GameManager()
    board = Board()
    # board.set_up_pieces()

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        board.draw(gm.screen)
        # board.draw_pieces(gm.screen)
        gm.loop()


if __name__ == "__main__":
    main()

