import unittest
from unittest.mock import patch
from io import StringIO
from logic import *


# class for testing
class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.board = create_grid()

    # Test for board initialization
    def test_init_board(self):
        empty_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(self.board, empty_board)

    # Test for player initialization and each player is assigned a unique piece to play
    @patch("builtins.input", side_effect=["X"])
    def test_symbol_selection(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.assertEqual(sym(), ("X", "O"))

    # Test for turns taking place by checking board to see that the next player has placed a piece
    @patch("builtins.input", side_effect=["0", "0", "0", "1"])
    def test_alternating_turns(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            startGamming(self.board, "X", "O", 0)
            self.assertEqual(self.board[0][0], "X")
            startGamming(self.board, "X", "O", 1)
            self.assertEqual(self.board[0][1], "O")

    # Test that a legal move was made after three illegal moves
    @patch("builtins.input", side_effect=["3", "0", "0", "-1", "0", "1", "0", "0"])
    def test_valid_move(self, mock_input):
        test_board = [[" ", "O", " "], [" ", " ", " "], [" ", " ", " "]]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            startGamming(test_board, "X", "O", 0)
            self.assertEqual(test_board[0][0], "X")

    # Test that a full board draw is identified
    def test_full_board_draw(self):
        tie_board = [["X", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]]
        self.assertEqual(isWinner(tie_board, "O", "X"), 0)

    # Test that all win cases are identified
    def test_player_wins(self):
        win_board = {}
        win_board[0] = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        win_board[1] = [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]]
        win_board[2] = [[" ", " ", " "], [" ", " ", " "], ["X", "X", "X"]]
        win_board[3] = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
        win_board[4] = [[" ", "X", " "], [" ", "X", " "], [" ", "X", " "]]
        win_board[5] = [[" ", " ", "X"], [" ", " ", "X"], [" ", " ", "X"]]
        win_board[6] = [["X", " ", " "], [" ", "X", " "], ["", "", "X"]]
        win_board[7] = [[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            for i in win_board:
                self.assertEqual(isWinner(win_board.get(i), "X", "O"), 1)


if __name__ == "__main__":
    unittest.main()
