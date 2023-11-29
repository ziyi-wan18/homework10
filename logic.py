def main():
    # The main function
    intro()
    board = create_grid()
    printPretty(board)
    symbol_1, symbol_2 = sym()
    isFull(
        board, symbol_1, symbol_2
    )  # The function that starts the game is also in here.


def intro():
    # This function introduces the rules of the game Tic Tac Toe
    print("Hello! Welcome to Tic Tac Toe!")
    print("\n")
    print(
        "Rules: Player 1 and player 2, represented by X and O, take turns "
        "marking the spaces in a 3*3 grid. The player who succeeds in placing "
        "three of their marks in a horizontal, vertical, or diagonal row wins."
    )


def create_grid():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def sym():
    # This function decides the players' symbols
    symbol_1 = input("Player 1, do you want to be X or O? ")
    while symbol_1 != "X" or symbol_1 != "x" or symbol_1 != "O" or symbol_1 != "o":
        if symbol_1 == "X" or "x":
            symbol_1 = symbol_1.upper()
            symbol_2 = "O"
            print("Player 1, you are " + symbol_1.upper())
            print("Player 2, you are " + symbol_2.upper())
            break
        elif symbol_1 == "O" or "o":
            symbol_1 = "O"
            symbol_2 = "X"
            print("Player 1, you are " + symbol_1.upper())
            print("Player 2, you are " + symbol_2.upper())
            break
        print("Please choose X or O.")
    return (symbol_1, symbol_2)


def startGamming(board, symbol_1, symbol_2, count):
    # This function starts the game.

    # Decides the turn
    if count % 2 == 0:
        player = symbol_1
    else:
        player = symbol_2
    print("Player " + player + ", it is your turn. ")
    # Check if players' selection is out of range
    while True:
        row = int(
            input(
                "Pick a row[upper row:"
                "[enter 0, middle row: enter 1, bottom row: enter 2]:"
            )
        )
        column = int(
            input(
                "Pick a column:"
                "[left column: enter 0, middle column: enter 1, right column enter 2]"
            )
        )
        if (
            (row > 2 or row < 0)
            or (column > 2 or column < 0)
            or (board[row][column] == symbol_1)
            or (board[row][column] == symbol_2)
        ):
            print("Invalid selection, please pick again.")
            continue
        else:
            break

    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1

    else:
        board[row][column] = symbol_2

    return board


def isFull(board, symbol_1, symbol_2):
    count = 0
    # This function check if the board is full
    while count < 10:
        startGamming(board, symbol_1, symbol_2, count)
        printPretty(board)
        count += 1
        if count == 9:
            print("The board is full. Game over.")

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2)

    if winner == 0:
        print("There is a tie.")
    elif winner == 1:
        print("Player " + symbol_1 + " won!")
    elif winner == 2:
        print("Player " + symbol_2 + " won!")


def printPretty(board):
    # This function prints the board nice!
    for r in range(len(board)):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        if r != 2:
            print("---+---+---")


def isWinner(board, symbol_1, symbol_2):
    # This function checks if any winner is winning
    winner = 0
    # Check the rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == symbol_1:
            winner = 1
        elif board[row][0] == board[row][1] == board[row][2] == symbol_2:
            winner = 2

    # Check the columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol_1:
            winner = 1
        elif board[0][col] == board[1][col] == board[2][col] == symbol_2:
            winner = 2

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = 1

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = 2

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = 1

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = 2

    return winner


if __name__ == "__main__":
    main()

