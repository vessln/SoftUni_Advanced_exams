def in_matrix(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(x) for x in input().split()]

field = []
boy_row, boy_col = 0, 0
is_collected = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for i in range(rows):
    line = list(input())
    if "B" in line:
        boy_row, boy_col = i, line.index("B")
    field.append(line)

start_row, start_col = boy_row, boy_col

while True:
    command = input()
    next_row = boy_row + directions[command][0]
    next_col = boy_col + directions[command][1]

    if not in_matrix(next_row, next_col):
        field[start_row][start_col] = " "
        print("The delivery is late. Order is canceled.")
        break

    if field[next_row][next_col] == "P":
        field[next_row][next_col] = "R"
        is_collected = True
        print("Pizza is collected. 10 minutes for delivery.")

    elif field[next_row][next_col] == "*":
        continue

    elif field[next_row][next_col] == "A":
        field[next_row][next_col] = "P"
        boy_row, boy_col = next_row, next_col
        print("Pizza is delivered on time! Next order...")
        break

    elif field[next_row][next_col] == "-":
        field[next_row][next_col] = "."

    boy_row, boy_col = next_row, next_col

[print(''.join(inner)) for inner in field]





