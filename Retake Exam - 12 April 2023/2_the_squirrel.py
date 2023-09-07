from collections import deque


def in_matrix(r, c, size_m):
    return 0 <= r < size_m and 0 <= c < size_m


size = int(input())
commands = deque(input().split(", "))
matrix = []
row_sq, col_sq = 0, 0
hazelnuts = 0
trap_or_out = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    line = list(input())
    matrix.append(line)
    if "s" in line:
        row_sq = i
        col_sq = line.index("s")

matrix[row_sq][col_sq] = "*"

while commands:
    command = commands.popleft()
    row_sq += directions[command][0]
    col_sq += directions[command][1]

    if not in_matrix(row_sq, col_sq, size):
        print("The squirrel is out of the field.")
        trap_or_out = True
        break

    else:

        if matrix[row_sq][col_sq] == "h":
            hazelnuts += 1
            matrix[row_sq][col_sq] = "*"
            if hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                break

        elif matrix[row_sq][col_sq] == "t":
            matrix[row_sq][col_sq] = "*"
            trap_or_out = True
            print("Unfortunately, the squirrel stepped on a trap...")

if len(commands) == 0 and hazelnuts < 3 and (not trap_or_out):
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")










