# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'
    
    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'
    
    # No winner found
    return None


def other_player(player):
    return 'O' if player == 'X' else 'X'

def print_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else ' ' for cell in row))
        print("-" * 9)

def get_player_move():
    row = int(input("Enter the row number (0, 1, or 2): "))
    col = int(input("Enter the column number (0, 1, or 2): "))
    return row, col

def update_board(board, row, col, player_symbol):
    board[row][col] = player_symbol
