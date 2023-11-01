import pygame as pg
from board import Board
from constants import SQUARE_SIZE, WHITE, BROWN, COLS, ROWS


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
        self.active_piece = None

    def loop(self):
        self.board.draw(self.screen)
        self.board.draw_pieces(self.screen)

        pg.display.flip()
        self.clock.tick(60)



    def calculate_board_possition(self, x, y):
        row = (y // SQUARE_SIZE)
        col = (x // SQUARE_SIZE)
        return row, col


    def handle_click(self, event):
                pos  = pg.mouse.get_pos()
                row, col = self.calculate_board_possition(pos[0], pos[1])

                self.board.selected = (row, col) #highlight square

                if self.board.board[row][col] != 0:
                    self.active_piece = self.board.board[row][col]

                    self._check_possible_moves(row, col)

    def update_position(self):
        if self.active_piece:
            old_row = self.active_piece.row
            old_col = self.active_piece.col

            pos = pg.mouse.get_pos()

            new_row, new_col = self.calculate_board_possition(pos[0], pos[1])

            self.active_piece.row = new_row
            self.active_piece.col = new_col

            self.board.board[old_row][old_col] = 0
            self.board.board[new_row][new_col] = self.active_piece

            self.active_piece.pos = (SQUARE_SIZE * new_col + SQUARE_SIZE // 2,
               SQUARE_SIZE * new_row + SQUARE_SIZE // 2)




    def _check_possible_moves(self, row, col):
        piece = self.board.board[row][col]
        possible_moves = []

        if piece.color == WHITE:
            #check move right (out perspective)
            if col + 1 < COLS and row + 1 < ROWS and self.board.board[row+1][col+1] == 0:
                possible_moves.append((row+1, col+1))

            #check move left
            if col - 1 >= 0 and row + 1 < ROWS and  self.board.board[row+1][col-1] == 0:
                possible_moves.append((row+1, col-1))

        else:
            # check move right (out perspective)
            if col + 1 < COLS and row - 1 >= 0 and self.board.board[row - 1][col + 1] == 0:
                possible_moves.append((row - 1, col + 1))

            # check move left
            if col - 1 >= 0 and row - 1 >= 0 and self.board.board[row - 1][col - 1] == 0:
                possible_moves.append((row - 1, col - 1))


        self.board.draw_possible_moves(possible_moves)


def main():
    gm = GameManager()

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gm.handle_click(event)

            elif event.type == pg.MOUSEBUTTONUP:
                gm.update_position()
                gm.active_piece = None

            elif event.type == pg.MOUSEMOTION:
                if gm.active_piece != None:
                    gm.active_piece.pos = pg.mouse.get_pos()

        gm.loop()


if __name__ == "__main__":
    main()

