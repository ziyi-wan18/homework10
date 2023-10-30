# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'

    while winner == None:
        print_board(board) 
        print(f"Player {current_player}'s turn:")
        row, col = get_player_move()
        update_board(board, row, col, current_player)  # Implement get_player_move() and   update_board() functions from previous response
        winner = get_winner(board) 
        current_player = other_player(current_player) 
        
        print_board(board)
        print(f"Player {winner} wins!")

      
