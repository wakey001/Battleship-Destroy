from random import randint


board = []
hidden_board = []


# "O" = Capital letter o
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


def get_ship_location():
    row = input("Please enter a row between 1-8: ")
    while row not in '12345678':
        print("Error enter a number between 1-8")
        row = input("Please enter a row between 1-8: ")
    col = input("Please enter a column between 1-8: ")
    while col not in '12345678':
        print("Error enter a number between 1-8")
        col = input("Please enter a number between 1-8: ")
    return int(row) - 1, int(col) - 1


def count_hit_ships(board):
    count = 0
    for row in board:
        for col in row:
            if col == "X":
                count += 1
    return count


create_ships(hidden_board)
turns = 10
print("Welcome to battleship")
print("---------------------")
while turns > 0:
    print_board(board)
    row, col = get_ship_location()
    if board[row][col] == '-':
        print("You guessed that already")
    elif hidden_board[row][col] == "X":
        print("congratulations, you hit the battleship")
        board[row][col] = "X"
        turns -= 1
    else:
        print("Sorry, you missed")
        board[row][col] = ' - '
        turns -= 1
        if count_hit_ships(board) == 5:
            print("Well done you sunk all the battleships")
            break
        print(f"You have {turns} turns left")
    

def quit_game():
    quit_game = input("Press Q to quit at any time")
    if quit_game == "Q":
        create_ships(board)    