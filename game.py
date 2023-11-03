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

                if self.board.board[row][col] != 0 and self.board.board[row][col].up == self.up:
                    mandatory_jumps = self.check_mandatory_jump()
                    if mandatory_jumps:
                        if (row, col) in mandatory_jumps:
                            self.active_piece = self.board.board[row][col]
                    else:
                        self.active_piece = self.board.board[row][col]

    def check_mandatory_jump(self):
        pieces = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.board[row][col] != 0 and self.board.board[row][col].up == self.up:
                    if self.possible_captures(row, col):
                        pieces.append((row, col))

        return pieces



    def possible_captures(self, row, col, king=False):
        captures = []

        if self.up:
            if row + 2 < ROWS and col + 2 < COLS:
                #right capture
                if self.board.board[row+1][col+1] != 0 and self.board.board[row+1][col+1].up != self.up \
                        and self.board.board[row+2][col+2] == 0:
                   captures.append((row+2, col+2))
            if row + 2 < ROWS and col - 2 >= 0:
                #left capture
                if self.board.board[row+1][col-1] != 0 and self.board.board[row+1][col-1].up != self.up \
                        and self.board.board[row+2][col-2] == 0:
                    captures.append((row + 2, col - 2))

            if king:
                if row - 2 >= 0 and col + 2 < COLS:
                    # right capture
                    if self.board.board[row - 1][col + 1] != 0 and self.board.board[row + 1][col + 1].up != self.up \
                            and self.board.board[row - 2][col + 2] == 0:
                        captures.append((row - 2, col + 2))
                if row - 2 >= 0 and col - 2 >= 0:
                    # left capture
                    if self.board.board[row - 1][col - 1] != 0 and self.board.board[row - 1][col - 1].up != self.up \
                            and self.board.board[row - 2][col - 2] == 0:
                        captures.append((row - 2, col - 2))

        else:
            if row - 2 >= 0 and col + 2 < COLS:
                # right capture
                if self.board.board[row - 1][col + 1] != 0 and self.board.board[row - 1][col + 1].up != self.up \
                        and self.board.board[row - 2][col + 2] == 0:
                    captures.append((row - 2, col + 2))
            if row - 2 >= 0 and col - 2 >= 0:
                # left capture
                if self.board.board[row - 1][col - 1] != 0 and self.board.board[row - 1][col - 1].up != self.up \
                        and self.board.board[row - 2][col - 2] == 0:
                    captures.append((row - 2, col - 2))

            if king:
                if row + 2 >= ROWS and col + 2 < COLS:
                    # right capture
                    if self.board.board[row + 1][col + 1] != 0 and self.board.board[row + 1][col + 1].up != self.up \
                            and self.board.board[row + 2][col + 2] == 0:
                        captures.append((row - 2, col + 2))
                if row + 2 < ROWS and col - 2 >= 0:
                    # left capture
                    if self.board.board[row - 1][col - 1] != 0 and self.board.board[row - 1][col - 1].up != self.up \
                            and self.board.board[row - 2][col - 2] == 0:
                        captures.append((row - 2, col - 2))

        return captures
    

    def update_position(self):
        old_row = self.active_piece.row
        old_col = self.active_piece.col

        pos = pg.mouse.get_pos()
        new_row, new_col = ((pos[1] // SQUARE_SIZE), (pos[0] // SQUARE_SIZE))

        normal_moves = self.posible_moves(old_row, old_col)
        capturing_moves = self.possible_captures(old_row, old_col)

        print('Normal: ', normal_moves)
        print('Capturing: ', capturing_moves)


        if len(capturing_moves) > 0:
            if (new_row, new_col) in capturing_moves:
                self.active_piece.row = new_row
                self.active_piece.col = new_col

                self.board.board[old_row][old_col] = 0
                self.board.board[new_row][new_col] = self.active_piece

                self.active_piece.pos = (SQUARE_SIZE * new_col + SQUARE_SIZE // 2,
                                         SQUARE_SIZE * new_row + SQUARE_SIZE // 2)
                self.board.board[(old_row + new_row) // 2][(old_col + new_col) // 2] = 0

                if not self.possible_captures(new_row, new_col, self.up):
                    self.up = not self.up
            else:
                self.active_piece.pos = (SQUARE_SIZE * old_col + SQUARE_SIZE // 2,
                                         SQUARE_SIZE * old_row + SQUARE_SIZE // 2)

        elif (new_row, new_col) in normal_moves:
            self.active_piece.row = new_row
            self.active_piece.col = new_col

            self.board.board[old_row][old_col] = 0
            self.board.board[new_row][new_col] = self.active_piece

            self.active_piece.pos = (SQUARE_SIZE * new_col + SQUARE_SIZE // 2,
                                     SQUARE_SIZE * new_row + SQUARE_SIZE // 2)

            self.up = not self.up


        else:
            self.active_piece.pos = (SQUARE_SIZE * old_col + SQUARE_SIZE // 2,
                                     SQUARE_SIZE * old_row + SQUARE_SIZE // 2)

        self.board.selected = None


    def posible_moves(self, row, col, king=False):
        possible_moves = []

        if self.up:
            # check normal moves
            #right move
            if row + 1 < ROWS and col + 1 < COLS:
                if self.board.board[row+1][col+1] == 0:
                    possible_moves.append((row+1, col+1))

            #left move
            if row + 1 < ROWS and col - 1 >= 0:
                if self.board.board[row+1][col-1] == 0:
                    possible_moves.append((row+1, col-1))

            if king:
                if row - 1 >= 0 and col + 1 >= 0:
                    if self.board.board[row - 1][col + 1] == 0:
                        possible_moves.append((row - 1, col + 1))
                if row - 1 >= 0 and col - 1 >= 0:
                    if self.board.board[row - 1][col - 1] == 0:
                        possible_moves.append((row - 1, col - 1))

        else:
            # right move
            if row - 1 >= 0 and col + 1 < COLS:
                if self.board.board[row - 1][col + 1] == 0:
                    possible_moves.append((row - 1, col + 1))
            if row - 1 >= 0 and col - 1 >= 0:
                if self.board.board[row - 1][col - 1] == 0:
                    possible_moves.append((row - 1, col - 1))

            if king:
                if row + 1 < ROWS and col + 1 < COLS:
                    if self.board.board[row - 1][col + 1] == 0:
                        possible_moves.append((row - 1, col + 1))
                if row + 1 < ROWS and col - 1 >= 0:
                    if self.board.board[row + 1][col - 1] == 0:
                        possible_moves.append((row + 1, col - 1))

        return possible_moves


