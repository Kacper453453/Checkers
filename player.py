from constants import SQUARE_SIZE
import pygame as pg
import random
import threading
from game import GameManager
from minimax import minimax

class Player(GameManager):
    def __init__(self, side, ai):
        super().__init__()
        self.side = side
        self.active = None
        self.ai = ai


    def player_move(self):
        ''''return:
            0 - no move
            1 - normal move
            2 - capturing move
            3 - capturing move with possible capture'''

        outcome = 0

        old_row, old_col = self.active.row, self.active.col
        pos = pg.mouse.get_pos()
        new_row, new_col = ((pos[1] // SQUARE_SIZE), (pos[0] // SQUARE_SIZE))

        moves = self.board.possible_moves(self.active)
        pieces = self.board.avaliable_pieces(self.side)

        if (new_row, new_col) in moves and self.active.compare(pieces):
            outcome += 1

            self.board.board[old_row][old_col] = 0
            self.board.board[new_row][new_col] = self.active
            self.board.update()

            if abs(new_row - old_row) > 1:
                outcome += 1

                captured_row, captured_col = (old_row + new_row) // 2, (old_col + new_col) // 2
                self.board.remove(captured_row, captured_col)


                pos_capture = self.board.possible_capture(self.active)
                print(pos_capture)
                if len(pos_capture) > 0:
                    outcome += 1

        else:
            self.active.update_pos(old_row, old_col)


        return outcome


    @staticmethod
    def _thread(func):
        def wrapper(*args, **kwargs):
            return threading.Thread(target=func, args=args, kwargs=kwargs).start()

        return wrapper

    @_thread
    def random_move(self):
        # chose random avaliable piece
        aval_pieces = self.board.avaliable_pieces(self.side)
        active_piece = random.choice(aval_pieces)

        # chose random move
        pos_moves = self.board.possible_moves(active_piece)
        move = random.choice(pos_moves)

        old_row, old_col = active_piece.row, active_piece.col
        new_row, new_col = move

        self.board.update()

        # check capture
        if abs(new_row - old_row) > 1:
            self.board.remove(active_piece, new_row, new_col)

            if self.board.possible_capture(active_piece):
                self.random_move()

    @_thread
    def _minimax(self, game):
        pg.time.delay(500)
        value, new_board, piece = minimax(self.board, 3, self.side,float('-inf'), float('inf'), game)

        old_row, old_col = piece.row, piece.col
        self.board.board = new_board.board
        self.board.update()
        new_row, new_col = piece.row, piece.col

        if abs(old_row - new_row) > 1:

            if self.board.possible_capture(piece):
                self._minimax(game)
































