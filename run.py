from random import randint


board = []
hidden_board = []


# "O" = Capital letter o
for i in range(8):
    hidden_board.append(["|"] * 8)
for i in range(8):
    board.append(["O"] * 8)  # Appends 8  * "O" to the empty-list board
# expected output["O", "O", "O", "O", "O"]


def print_board(board):
    for row in board:
        print(" ".join(row))  # Gets rid or the "" and inserts whitspace


def create_ships(board):
    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = "X"


def get_ship_location():
    guess_row = input("Please enter a row between 1-8: ")
    while guess_row not in '12345678':
        print("Error enter a number between 1-8")
        guess_row = input("Please enter a row between 1-8: ")
    guess_col = input("Please enter a column between 1-8: ")
    while guess_col not in '12345678':
        print("Error enter a number between 1-8")
    guess_col = input("Please enter a number between 1-8: ")
    return int(guess_row) - 1, int(guess_col) - 1


def count_hit_ships(board):
    count = 0
    for row in board:
        for col in row:
            if col == "X":
                count += 1
    return count


create_ships(hidden_board)
turns = 10
while turns > 0:
    print("Welcome to battleship")
    print("---------------------")
    print_board(board)
    print_board(hidden_board)
    row, col = get_ship_location()
    if board[row][col] == '-':
        print("You guessed that already")
    elif hidden_board[row][col] == "X":
        print("congratulations, you hit the battleship")
        board[row][col] = "X"
        turns -= 1





