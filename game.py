import pygame as pg
from board import Board
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,SQUARE_SIZE, COLS, ROWS

class GameManager:
    def __init__(self):
        pg.display.set_caption('Checkers')
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

        self.board = Board()
        self.board.set_up_pieces()
        self.active_piece = None
        self.up = True

    def loop(self):
        self.board.draw(self.board.board_surface)
        self.board.draw_pieces(self.board.board_surface)

        self.screen.blit(self.board.board_surface, (0, 0))
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


    def handle_click(self):
                pos  = pg.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE

                self.board.selected = (row, col) #highlight square


                if self.board.board[row][col] != 0:
                    if self.board.board[row][col].up == self.up:

                        self.active_piece = self.board.board[row][col]
                        self.possible_moves = self._check_possible_moves(row, col)  # -> ['-32'] or ['x32]


    def update_position(self):
        old_row = self.active_piece.row
        old_col = self.active_piece.col

        pos = pg.mouse.get_pos()
        new_row, new_col = ((pos[1] // SQUARE_SIZE), (pos[0] // SQUARE_SIZE))


        new_pos_notation = self._covert_notation((old_row, old_col), (new_row, new_col))

        if new_pos_notation in self.possible_moves:

            self.active_piece.row = new_row
            self.active_piece.col = new_col

            self.board.board[old_row][old_col] = 0
            self.board.board[new_row][new_col] = self.active_piece

            self.active_piece.pos = (SQUARE_SIZE * new_col + SQUARE_SIZE // 2,
               SQUARE_SIZE * new_row + SQUARE_SIZE // 2)



            if new_pos_notation[0] =='x':
                self.board.board[(old_row + new_row)//2][(old_col + new_col)//2] = 0

                if not self.possible_captures(new_row, new_col, self.up):
                    self.up = not self.up
            else:
                self.up = not self.up

        else:
            self.active_piece.pos = (SQUARE_SIZE * old_col + SQUARE_SIZE // 2,
               SQUARE_SIZE * old_row + SQUARE_SIZE // 2)

        self.board.selected = None



    def _covert_notation(self, old, new):
        if abs(old[0] - new[0]) > 1:
            return f'x{new[0]}{new[1]}'
        else:
            return f'-{new[0]}{new[1]}'

    def possible_captures(self, row, col, up: bool):
        captures = []
        color = self.active_piece.color

        if up:
            if row + 2 < ROWS and col + 2 < COLS:
                #right capture
                if self.board.board[row+1][col+1] != 0 and self.board.board[row+1][col+1].color != color \
                        and self.board.board[row+2][col+2] == 0:
                   captures.append(self._covert_notation((row, col), (row+2, col+2)))
            if row + 2 < ROWS and col - 2 >= 0:
                #left capture
                if self.board.board[row+1][col-1] != 0 and self.board.board[row+1][col-1].color != color \
                        and self.board.board[row+2][col-2] == 0:
                    captures.append(self._covert_notation((row, col), (row + 2, col - 2)))
        else:
            if row - 2 >= 0 and col + 2 < COLS:
                # right capture
                if self.board.board[row - 1][col + 1] != 0 and self.board.board[row - 1][col + 1].color != color \
                        and self.board.board[row - 2][col + 2] == 0:
                    captures.append(self._covert_notation((row, col), (row - 2, col + 2)))
            if row - 2 >= 0 and col -2 >= 0:
                # left capture
                if self.board.board[row - 1][col - 1] != 0 and self.board.board[row - 1][col - 1].color != color \
                        and self.board.board[row - 2][col - 2] == 0:
                    captures.append(self._covert_notation((row, col), (row - 2, col - 2)))

        return captures


    def _check_possible_moves(self, row, col):
        '''notation -> -22 - means row=row col=col moves to row=2 col=2
                        x22 - means row=row col=col captures row=2 col=2'''

        piece = self.active_piece
        possible_moves = []
        possible_captures = self.possible_captures(row, col, piece.up)

        if len(possible_captures) > 0:
            return possible_captures


        if self.up:
            # check normal moves
            #right move
            if row + 1 < ROWS and col + 1 < COLS:
                if self.board.board[row+1][col+1] == 0:
                    possible_moves.append(f'-{row+1}{col+1}')

            #left move
            if row + 1 < ROWS and col - 1 >= 0:
                if self.board.board[row+1][col-1] == 0:
                    possible_moves.append(f'-{row+1}{col-1}')

        else:
            # right move
            if row - 1 >= 0 and col + 1 < COLS:
                if self.board.board[row - 1][col + 1] == 0:
                    possible_moves.append(f'-{row - 1}{col + 1}')
            if row - 1 >= 0 and col - 1 >= 0:
                if self.board.board[row - 1][col - 1] == 0:
                    possible_moves.append(f'-{row - 1}{col - 1}')

        return possible_moves


