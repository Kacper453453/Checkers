import pygame as pg
from game import GameManager
from player import Player
pg.init()


def main():
    gm = GameManager()

    player1 = Player('up', ai=True)
    player2 = Player('down', ai=False)

    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            # timer event
            if event.type == pg.USEREVENT:
                if gm.turn == player2.side:
                    gm.timer_up_text.set_alpha(128)
                    gm.curent_seconds_down -= 1
                else:
                    gm.timer_down_text.set_alpha(128)
                    gm.curent_seconds_up -= 1

            gm.handle_player_event(event, player1)
            gm.handle_player_event(event, player2)

            if winner:=gm.check_winner() != None:
                print(winner)
                run = False

        gm.loop()

if __name__ == "__main__":
    main()