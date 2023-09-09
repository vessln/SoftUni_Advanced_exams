def in_matrix(r, c, size_m):
    return 0 <= r < size_m and 0 <= c < size_m


text = list(input())
size = int(input())
matrix = []
my_row, my_col = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    line = list(input())
    matrix.append(line)

    if "P" in line:
        my_row, my_col = i, line.index("P")

matrix[my_row][my_col] = "-"

turns = int(input())

for i in range(turns):
    command = input()
    next_row = directions[command][0] + my_row
    next_col = directions[command][1] + my_col

    if in_matrix(next_row, next_col, size):
        if matrix[next_row][next_col] != "-":
            letter = matrix[next_row][next_col]
            text.append(letter)
            matrix[next_row][next_col] = "-"

        my_row, my_col = next_row, next_col

    else:
        if text:
            text.pop()

matrix[my_row][my_col] = "P"

print(''.join(text))
[print(''.join(el)) for el in matrix]







