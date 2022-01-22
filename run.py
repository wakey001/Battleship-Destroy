from random import randint


board = []
hidden_board = []
users_board = []


# "O" = Capital letter o
for i in range(8):
    users_board.append(["U"] * 8)
for i in range(8):
    hidden_board.append(["H"] * 8)
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


def create_user_ships(board):
    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while users_board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        users_board[ship_row][ship_col] = "X"


def computer_guess():
    computer_row, computer_col = randint(1, 8), randint(1, 8)
    print("The computer guessed")
    print("row " + str(computer_row) + " "  "col " + str(computer_col))
    return int(computer_row) - 1, int(computer_col) - 1


def get_ship_location(): 
    row = input("Please enter a row between 1-8:\n")
    while row not in '1, 2, 3, 4, 5, 6, 7, 8':
        print("Error enter a number between 1-8")
        row = input("Please enter a row between 1-8:\n")
    col = input("Please enter a column between 1-8:\n")
    while col not in '1, 2, 3, 4, 5, 6, 7, 8':
        print("Error enter a number between 1-8")
        col = input("Please enter a number between 1-8:\n")
    return int(row) - 1, int(col) - 1


def count_hit_ships(board):
    count = 0
    for row in board:
        for col in row:
            if col == "X":
                count += 1
    return count


def count_hit_user_ships(users_board):
    user_count = 0
    for row in users_board:
        for col in row:
            if col == "X":
                user_count += 1
    return user_count


def did_computer_hit():
    if users_board[row][col] == "X":
        print("Computer hit a battleship you have \n")
        users_board[row][col] = "X"
    if users_board[row][col] == "U":
        print("computer missed ")
        users_board[row][col] = "-"


def get_user_name():
    user_name = ""
    user_name = input("What is your name:\n")
    if user_name == "":
        user_name = input("What is your name:\n")
    else:
        print(user_name + "'s board")
    return user_name


create_user_ships(users_board)
create_ships(hidden_board)
turns = 10
print("Welcome to battleship")
print("Hit 5 ships within " + str(turns) + " turns")
get_user_name()
while turns > 0:
    print_board(users_board)
    print("---------------------")
    print_board(board)
    print("---------------------")
    row, col = get_ship_location()
    if board[row][col] == '-':
        print("You guessed that already")
        computer_guess()
    elif hidden_board[row][col] == "X":
        print("You hit the battleship you have " + str(turns) + " turns left")
        board[row][col] = "X"
        turns -= 1
        computer_guess()
    else:
        print("Sorry, you missed you have " + str(turns) + " turns left")
        board[row][col] = '-'
        turns -= 1
        computer_guess()
    if count_hit_ships(board) == 5:
        print("Well done you sunk all the battleships")
        break
