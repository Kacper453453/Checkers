import pygame as pg
from piece import Piece
from constants import ROWS, COLS, SQUARE_SIZE, LIGHT_GREEN, BLACK, LIGHT_BROWN


class Board:
    def __init__(self):
        self.board = []
        self.highlight = None

    def draw(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    pg.draw.rect(surface, BLACK,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                    # highlight selected square
                    if (row, col) == self.highlight:
                        pg.draw.rect(surface, LIGHT_GREEN,
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pg.draw.rect(surface, LIGHT_BROWN,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def mandatory_moves(self, side):
        for piece in self.pieces_status(side):
            if self.possible_capture(piece):
                return True


    def evaluate(self):
        comp_status = self.pieces_status('up')
        player_status = self.pieces_status('down')

        comp_left = len(comp_status)
        player_left = len(player_status)
        comp_king = sum([1 for piece in comp_status if piece.king])
        player_king = sum([1 for piece in player_status if piece.king])

        return comp_left - player_left + 0.5 * (comp_king - player_king)

    def update(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.row = row
                    piece.col = col
                    piece.update_pos(row, col)


    def draw_possible_moves(self, moves):
        pass

    def pieces_status(self, side):
        status = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    if self.board[row][col].side == side:
                        status.append(self.board[row][col])
        return status

    def set_up_pieces(self):
        for row in range(ROWS):
            board_row = []
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        board_row.append(Piece(row, col, 'up'))
                    elif row > 4:
                        board_row.append(Piece(row, col, 'down'))
                    else:
                        board_row.append(0)
                else:
                    board_row.append(0)
            self.board.append(board_row)


    def draw_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    piece = self.board[row][col]
                    piece.draw(surface)

    def remove(self, row, col):
        self.board[row][col] = 0

    def avaliable_pieces(self, side):
        mandatory = []
        normal = []

        for piece in self.pieces_status(side):

            captures = self.possible_capture(piece)
            moves = self.possible_moves(piece)
            if captures:
                mandatory.append(piece)
            if moves:
                normal.append(piece)


        return mandatory if len(mandatory) > 0 else normal

    def possible_moves(self,piece):

        captures = self.possible_capture(piece)
        normal_moves = self.posible_normal_move(piece)
        return captures if captures else normal_moves

    def posible_normal_move(self, piece):
        possible_moves = []
        row, col = piece.row, piece.col
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        turn = piece.side

        for direction in directions:
            row_dir, col_dir = direction
            next_row, next_col = row + row_dir, col + col_dir

            if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                if self.board[next_row][next_col] == 0:
                    if piece.king:
                        possible_moves.append((next_row, next_col))
                    elif turn == 'up' and row < next_row:
                        possible_moves.append((next_row, next_col))
                    elif turn != 'up' and row > next_row:
                        possible_moves.append((next_row, next_col))

        return possible_moves

    def possible_capture(self, piece):
        captures = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        row, col = piece.row, piece.col
        turn = piece.side

        for direction in directions:
            row_dir, col_dir = direction
            capture_row, capture_col = row + row_dir, col + col_dir
            next_row, next_col = row + 2 * row_dir, col + 2 * col_dir

            if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                if self.board[capture_row][capture_col] != 0 and self.board[capture_row][
                    capture_col].side != turn \
                        and self.board[next_row][next_col] == 0:
                    if piece.king:
                        captures.append((next_row, next_col))
                    elif turn == 'up' and row < next_row:
                        captures.append((next_row, next_col))
                    elif turn != 'up' and row > next_row:
                        captures.append((next_row, next_col))

        return captures


