def in_playground(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(x) for x in input().split()]
my_row, my_col = 0, 0
touched_players, moves = 0, 0
matrix = []

for i in range(rows):
    line = input().split()

    if "B" in line:
        my_row, my_col = i, line.index("B")

    matrix.append(line)

matrix[my_row][my_col] = "-"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while touched_players < 3:
    command = input()
    if command == "Finish":
        break

    next_row = directions[command][0] + my_row
    next_col = directions[command][1] + my_col

    if in_playground(next_row, next_col):

        if matrix[next_row][next_col] == "P":
            touched_players += 1
            moves += 1
            matrix[next_row][next_col] = "-"
            my_row, my_col = next_row, next_col

        elif matrix[next_row][next_col] == "-":
            moves += 1
            my_row, my_col = next_row, next_col

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")


