def print_matrix():
    print("-"*9)
    for row in matrix:
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("-"*9)


def enter_coordinates():
    while True:
        entries = input("Enter the coordinates: ").split()
        if entries[0].isdigit() and entries[1].isdigit():
            x, y = [int(entry) for entry in entries[:2]]
            if 1 <= x <= 3 and 1 <= y <= 3:
                if matrix[x-1][y-1] == " ":
                    return x - 1, y - 1
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


def draw():
    if all(cell != " " for row in matrix for cell in row):
        print("Draw")
        return True


def win(player):
    if any(all(cell == player for cell in row) for row in matrix) or \
            any(all(row[i] == player for row in matrix) for i in range(3)) or \
            all(matrix[i][i] == player for i in range(3)) or \
            all(matrix[i][2-i] == player for i in range(3)):
        print(player, "wins")
        return True


matrix = [[" "] * 3 for _ in range(3)]
print_matrix()
player = "X"
while True:
    x, y = enter_coordinates()
    matrix[x][y] = player
    print_matrix()
    if win(player) or draw():
        break
    player = "O" if player == "X" else "X"

