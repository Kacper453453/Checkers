
import pygame as pg
from board import Board
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,SQUARE_SIZE, COLS, ROWS, BOARD_SIZE, WHITE
import random
import threading


class GameManager:
    _shared_board = Board()
    _turn = random.choice(['up', 'down'])

    def __init__(self):
        super().__init__()
        pg.display.set_caption('Checkers')
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font("freesansbold.ttf", 32)
        self.board = self._shared_board
        self.board.set_up_pieces()
        self.player_score = self.comp_score = 0

        self.turn = self._turn
        pg.time.set_timer(pg.USEREVENT, 1000)

        self.curent_seconds_up = 180
        self.curent_seconds_down = 180

        self.timer_up_text = self.timer_down_text = self.font.render("3:00", True, WHITE)
        self.timer_up_rect = self.timer_up_text.get_rect(center=(BOARD_SIZE+100, SCREEN_HEIGHT//2-100))
        self.timer_down_rect = self.timer_down_text.get_rect(center=(BOARD_SIZE+100, SCREEN_HEIGHT//2+100))

        self.thread_event = threading.Event()
    def display_time(self):

        display_seconds_up = self.curent_seconds_up % 60
        display_minutes_up = int(self.curent_seconds_up / 60) % 60
        display_seconds_down = self.curent_seconds_down % 60
        display_minutes_down = int(self.curent_seconds_down / 60) % 60

        timer_up = self.font.render(f"{display_minutes_up}:{display_seconds_up:02d}", True, WHITE)
        self.screen.blit(timer_up, self.timer_up_rect)

        timer_down= self.font.render(f"{display_minutes_down}:{display_seconds_down:02d}", True, WHITE)
        self.screen.blit(timer_down, self.timer_down_rect)

    def handle_player_event(self, event, player):
        if player.ai == False:
            # player event
            if self.turn == player.side:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(player)

                if event.type == pg.MOUSEMOTION:
                    if player.active:
                        player.active.pos = pg.mouse.get_pos()

                if event.type == pg.MOUSEBUTTONUP and player.active:
                    player_move = player.player_move()
                    if 0 < player_move < 3:
                        self.switch_turn()
                    player.active = None

        else:
            # computer event
            if self.turn == player.side:
                self.thread_event.set()
                player._minimax(self)
                self.thread_event.wait()

                self.switch_turn()

    def switch_turn(self):
        # self.turn = 'up' if 'down' else 'up'
        if self.turn == 'up':
            self.turn = 'down'
        elif self.turn == 'down':
            self.turn = 'up'

        print("Turn: ", self.turn)


    def check_winner(self):
        if self.player_score == 8:
            return 'down'
        elif self.comp_score == 8:
            return 'up'
        elif self.curent_seconds_up == 0:
            return 'down'
        elif self.curent_seconds_down == 0:
            return 'up'

        return None


    def loop(self):
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)
        self.board.draw_pieces(self.screen)
        self.check_king()
        self.display_time()

        pg.display.flip()
        self.clock.tick(60)

    def handle_click(self, player):
        if player.turn:
            pos = pg.mouse.get_pos()

            row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
            self.board.selected = (row, col)

            if self.board.board[row][col] != 0 and self.board.board[row][col].side == player.side:

                player.active = self.board.board[row][col]

    def pieces_status(self, side):
        status = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.board[row][col] != 0:
                    if self.board.board[row][col].side == side:
                        status.append(self.board.board[row][col])
        return status

    def check_king(self):

        for row in range(ROWS):
            for col in range(COLS):
                if self.board.board[row][col] != 0:
                    piece = self.board.board[row][col]
                    if piece.side == 'up':
                        if piece.row == 7:
                            piece.king = True
                    else:
                        if piece.row == 0:
                            piece.king = True


