# import random

board = []
# "O" = Capital letter o

for i in range(5):
    board.append(["O"] * 5)  # Appends 5 * "O" to the empty-list board
# expected output["O", "O", "O", "O", "O"]


def print_board(board):
    for row in board:
        print(" ".join(row))  # Gets rid or the "" and inserts whitspace


print_board(board)
