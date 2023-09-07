def in_battlefield(r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())
matrix = []
my_row, my_col = 0, 0
mines = 0
cruisers = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    line = list(input())
    matrix.append(line)

    if "S" in line:
        my_row = i
        my_col = line.index("S")

matrix[my_row][my_col] = "-"

while True:
    command = input()

    new_row = directions[command][0] + my_row
    new_col = directions[command][1] + my_col

    if in_battlefield(new_row, new_col):

        if matrix[new_row][new_col] == "-":
            my_row, my_col = new_row, new_col

        elif matrix[new_row][new_col] == "C":
            matrix[new_row][new_col] = "-"
            my_row, my_col = new_row, new_col
            cruisers += 1
            if cruisers == 3:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                break

        elif matrix[new_row][new_col] == "*":
            matrix[new_row][new_col] = "-"
            my_row, my_col = new_row, new_col
            mines += 1
            if mines == 3:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
                break

matrix[my_row][my_col] = "S"
[print("".join(inner_list)) for inner_list in matrix]









