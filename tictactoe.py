"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    # Check if move is valid
    if board[i][j] != EMPTY:
        raise Exception("Invalid move")
    
    # Create a deep copy
    new_board = copy.deepcopy(board)
    
    # Make the move
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
    
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there's a winner, game is over
    if winner(board) is not None:
        return True
    
    # Check if board is full
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X wants to maximize
        value, action = max_value(board)
        return action
    else:
        # O wants to minimize
        value, action = min_value(board)
        return action


def max_value(board):
    """
    Helper function for minimax - maximizes for player X.
    """
    if terminal(board):
        return utility(board), None
    
    best_value = -float('inf')
    best_action = None
    
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        
        if min_val > best_value:
            best_value = min_val
            best_action = action
            
            # Alpha-beta pruning
            if best_value == 1:
                break
    
    return best_value, best_action


def min_value(board):
    """
    Helper function for minimax - minimizes for player O.
    """
    if terminal(board):
        return utility(board), None
    
    best_value = float('inf')
    best_action = None
    
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        
        if max_val < best_value:
            best_value = max_val
            best_action = action
            
            # Alpha-beta pruning
            if best_value == -1:
                break
    
    return best_value, best_action
