# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import create_grid, isWinner, startGamming

def print_board(board):
    # Print the Tic Tac Toe board
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("---------")

def get_player_move():
    # Get the player's move (row and column)
    row = int(input("Pick a row [0, 1, 2]: "))
    col = int(input("Pick a column [0, 1, 2]: "))
    return row, col

def update_board(board, row, col, current_player):
    # Update the board with the player's move
    board[row][col] = current_player

if __name__ == '__main__':
    board = create_grid()
    winner = None
    current_player = 'X'

    while winner is None:
        print_board(board)
        print(f"Player {current_player}'s turn:")
        row, col = get_player_move()
        startGamming(board, 'X', 'O', 1)  # Use startGamming function from logic.py
        winner = isWinner(board, 'X', 'O')
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    if winner == 'X' or winner == 'O':
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

      
