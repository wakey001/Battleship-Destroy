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


# Assign both functions above to respective variables


ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)
guess_row = int(input("Guess Row: "))  # User to guess a Row 
guess_col = int(input("Guess Col: "))  # User to guess a Col

if guess_row == ship_row and guess_col == guess_col:
    print("Well done you found and destroyed the battleship!")
    

