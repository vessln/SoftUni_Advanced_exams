def in_matrix(r, c, SIZE):
    return 0 <= r < SIZE and 0 <= c < SIZE


def opposite_side(row, col, SIZE):
    if row < 0:
        row = SIZE - 1
    elif row >= SIZE:
        row = 0
    elif col < 0:
        col = SIZE - 1
    elif col >= SIZE:
        col = 0

    return row, col


SIZE = 6
matrix = []
my_row, my_col = 0, 0
water, metal, concrete = 0, 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(SIZE):
    line = input().split()
    matrix.append(line)

    if 'E' in line:
        my_row = i
        my_col = line.index('E')

all_commands = input().split(', ')

for command in all_commands:
    my_row += directions[command][0]
    my_col += directions[command][1]

    if not in_matrix(my_row, my_col, SIZE):
        new_row, new_col = opposite_side(my_row, my_col, SIZE)
        my_row, my_col = new_row, new_col

    if in_matrix(my_row, my_col, SIZE):
        if matrix[my_row][my_col] == 'W':
            water += 1
            print(f"Water deposit found at ({my_row}, {my_col})")
        elif matrix[my_row][my_col] == 'M':
            metal += 1
            print(f"Metal deposit found at ({my_row}, {my_col})")
        elif matrix[my_row][my_col] == 'C':
            concrete += 1
            print(f"Concrete deposit found at ({my_row}, {my_col})")
        elif matrix[my_row][my_col] == 'R':
            print(f"Rover got broken at ({my_row}, {my_col})")
            break

if all([water, metal, concrete]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")