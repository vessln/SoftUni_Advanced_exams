from math import floor


def in_matrix(r, c, size_):
    return 0 <= r < size_ and 0 <= c < size_


def opposite_side(row, col, size):
    if row >= size:
        row = 0
    if row < 0:
        row = size - 1
    if col >= size:
        col = 0
    if col < 0:
        col = size - 1
    return row, col


size = int(input())
matrix = []
my_row, my_col = 0, 0
path = []
coins = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    line = input().split()
    matrix.append(line)

    if "P" in line:
        my_row, my_col = i, line.index("P")

matrix[my_row][my_col] = "0"
path.append([my_row, my_col])

while True:
    command = input()

    if command in directions.keys():
        next_row = directions[command][0] + my_row
        next_col = directions[command][1] + my_col

        if in_matrix(next_row, next_col, size):
            my_row, my_col = next_row, next_col
        else:
            my_row, my_col = opposite_side(next_row, next_col, size)

        path.append([my_row, my_col])

        if matrix[my_row][my_col] == "X":
            if coins > 0:
                coins = floor(coins / 2)
            break

        else:
            num = int(matrix[my_row][my_col])
            coins += num

        matrix[my_row][my_col] = "0"

        if coins >= 100:
            break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for el in path:
    print(el)






