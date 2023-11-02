import pygame as pg
from board import Board
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,SQUARE_SIZE, WHITE, COLS, ROWS

class GameManager:
    def __init__(self):
        pg.display.set_caption('Checkers')
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

        self.board = Board()
        self.board.set_up_pieces()
        self.active_piece = None

        self.white_turn = True

    def loop(self):
        self.board.draw(self.screen)
        self.board.draw_pieces(self.screen)

        pg.display.flip()
        self.clock.tick(60)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_click()

        elif event.type == pg.MOUSEBUTTONUP:
            if self.active_piece != None:
                self.update_position()
                self.active_piece = None

        elif event.type == pg.MOUSEMOTION:
            if self.active_piece != None:
                self.active_piece.pos = pg.mouse.get_pos()


    def calculate_board_possition(self, x, y):
        row = (y // SQUARE_SIZE)
        col = (x // SQUARE_SIZE)
        return row, col


    def handle_click(self):
                pos  = pg.mouse.get_pos()
                row, col = self.calculate_board_possition(pos[0], pos[1])

                self.board.selected = (row, col) #highlight square

                if self.board.board[row][col] != 0:
                    if self.white_turn:
                        if self.board.board[row][col].color == WHITE:
                            self.active_piece = self.board.board[row][col]
                    else:
                        if self.board.board[row][col].color != WHITE:
                            self.active_piece = self.board.board[row][col]


    def update_position(self):
        old_row = self.active_piece.row
        old_col = self.active_piece.col

        possible_moves = self._check_possible_moves(old_row, old_col)

        pos = pg.mouse.get_pos()
        new_row, new_col = self.calculate_board_possition(pos[0], pos[1])

        if (new_row, new_col) in possible_moves:

            self.active_piece.row = new_row
            self.active_piece.col = new_col

            self.board.board[old_row][old_col] = 0
            self.board.board[new_row][new_col] = self.active_piece

            self.active_piece.pos = (SQUARE_SIZE * new_col + SQUARE_SIZE // 2,
               SQUARE_SIZE * new_row + SQUARE_SIZE // 2)
            self.white_turn = not self.white_turn
        else:
            self.active_piece.pos = (SQUARE_SIZE * old_col + SQUARE_SIZE // 2,
               SQUARE_SIZE * old_row + SQUARE_SIZE // 2)


        self.board.selected = None


    def _check_possible_moves(self, row, col):
        piece = self.board.board[row][col]
        possible_moves = []
        possible_captures = []

        if piece.color == WHITE:
            #check move right and right capture(out perspective)
            if col + 1 < COLS and row + 1 < ROWS:
                if self.board.board[row+1][col+1] == 0:
                    possible_moves.append((row+1, col+1))
                elif row + 2 < ROWS and col + 2 < COLS:
                    if self.board.board[row+2][col+2] == 0:

                        possible_moves.append((row+2, col+2))

            #check move left and left capture
            if col - 1 >= 0 and row + 1 < ROWS:
                if self.board.board[row+1][col-1] == 0:
                    possible_moves.append((row+1, col-1))

                elif row + 2 < ROWS and col - 2 >= 0:
                    if self.board.board[row+2][col-2] == 0:
                        #left capture

                        possible_moves.append((row+2, col-2))


        else:
            # check move right and right capture (out perspective)
            if col + 1 < COLS and row - 1 >= 0:
                if  self.board.board[row - 1][col + 1] == 0:
                    possible_moves.append((row - 1, col + 1))

                elif row - 2 >= 0 and col + 2 < COLS:
                    if self.board.board[row-2][col+2] == 0:
                        #right capture

                        possible_moves.append((row-2, col+2))

            # check move left
            if col - 1 >= 0 and row - 1 >= 0:
                if self.board.board[row - 1][col - 1] == 0:
                    possible_moves.append((row - 1, col - 1))

                elif row - 2 >= 0 and col - 2 >= 0:
                    if self.board.board[row-2][col-2] == 0:
                        #left capture

                        possible_moves.append((row-2, col-2))

        print(possible_moves)

        return possible_moves
