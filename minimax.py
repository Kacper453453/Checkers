from copy import deepcopy


def minimax(position ,depth, max_player, alpha, beta, game):


    if depth == 0 or game.check_winner() != None:
        return position.evaluate(), position.board, None


    if max_player:
        maxEval = float('-inf')
        best_move = None
        best_piece = None


        for move, piece in get_all_moves(position, 'up'):
            evaluation, resulting_board, moved_piece = minimax(move, depth-1, False, alpha, beta, game)[:3]

            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
                best_piece = piece

            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break

        return maxEval, best_move, best_piece

    else:
        minEval = float('inf')
        best_move = None
        best_piece = None

        for move, piece in get_all_moves(position, 'down'):
            evaluation, resulting_board, moved_piece = minimax(move, depth - 1, True, alpha, beta, game)[:3]

            if evaluation < minEval:
                minEval = evaluation
                best_move = move
                best_piece = piece

            beta = min(beta, evaluation)
            if beta <= alpha:
                break

        return minEval, best_move, best_piece



def get_all_moves(board, side):
    moves = []
    for piece in board.avaliable_pieces(side):
        valid_moves = board.possible_moves(piece)
        for move in valid_moves:

            temp_board = deepcopy(board)

            new_board = simulate_move(piece, move, temp_board)
            moves.append([new_board, piece])

    return moves

def simulate_move(piece, move, board):
    board.board[piece.row][piece.col] = 0
    board.board[move[0]][move[1]] = piece

    if abs(piece.row - move[0]) > 1:
        board.remove((piece.row + move[0])//2, (piece.col + move[1])//2)

    return board







