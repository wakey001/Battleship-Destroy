import random

'Empty list for the gameboard'

board = []
for i in range(5):
    board.append(['O'] * 5)

'Gets rid or the "" and inserts whitspace '
def print_board(board):
    for row in board:
        print(" ".join(row))


