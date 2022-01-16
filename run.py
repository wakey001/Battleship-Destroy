from random import randint

board = []
# "O" = Capital letter o

for i in range(5):
    board.append(["O"] * 5)  # Appends 5 * "O" to the empty-list board
# expected output["O", "O", "O", "O", "O"]


def print_board(board):
    for row in board:
        print(" ".join(row))  # Gets rid or the "" and inserts whitspace


def random_row(board):
    return randint(0, len(board) - 1)  # Random integer within the board, Row


def random_col(board):
    return randint(0, len(board[0]) - 1)  # Random int within the board, Col


print(random_row(board))


random_col(board)