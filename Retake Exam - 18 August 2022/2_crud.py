def is_in_matrix(r, c, SIZE):
    return 0 <= r < SIZE and 0 <= c < SIZE


SIZE = 6
matrix = [[el for el in input().split()] for _ in range(SIZE)]
my_position = input().strip(")(")
my_row, my_col = [int(x) for x in my_position.split(", ")]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command, *info = input().split(", ")
    if command == "Stop":
        break

    if is_in_matrix(my_row, my_col, SIZE):

        if command == "Create":
            move, value = info[0], info[1]
            my_row += directions[move][0]
            my_col += directions[move][1]
            if matrix[my_row][my_col] == ".":
                matrix[my_row][my_col] = value

        elif command == "Update":
            move, value = info[0], info[1]
            my_row += directions[move][0]
            my_col += directions[move][1]
            if matrix[my_row][my_col] != ".":
                matrix[my_row][my_col] = value

        elif command == "Delete":
            move = info[0]
            my_row += directions[move][0]
            my_col += directions[move][1]
            if matrix[my_row][my_col] != ".":
                matrix[my_row][my_col] = "."

        elif command == "Read":
            move = info[0]
            my_row += directions[move][0]
            my_col += directions[move][1]
            if matrix[my_row][my_col] != ".":
                print(matrix[my_row][my_col])

[print(*inner_list) for inner_list in matrix]

# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .
# (2, 3)
# Create, down, o
# Delete, right
# Read, up
# Create, left, 20
# Update, up, P
# Stop
