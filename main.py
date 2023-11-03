import pygame as pg
from game import GameManager
pg.init()

def main():
    gm = GameManager()

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            gm.handle_event(event)

        gm.loop()


if __name__ == "__main__":
    main()

