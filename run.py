from random import randint

turns = 5
board = []
# "O" = Capital letter o

for i in range(8):
    board.append(["O"] * 8)  # Appends 5 * "O" to the empty-list board
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
guess_row = int(input("Guess Row: "))  # User to guess a Row 
guess_col = int(input("Guess Col: "))  # User to guess a Col
print(ship_row)
print(ship_col)

if guess_row == ship_row and guess_col == ship_col:
    print("Well done you found and destroyed the battleship!")
else:
    if (guess_row < 0 or guess_row) > 4 or (guess_col < 0 and guess_col) > 4:
        print("That co-ordinate is off the board please try again")
    elif(board[guess_row][guess_col]) == "!":
        print("Already guessed here, try again.")
    else: 
        print("You missed the battleship!")
        board[guess_row][guess_col] = "!"
    print_board(board)
    




    

