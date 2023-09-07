def is_in_matrix(r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())
num_car = input()
matrix = []
car_row, car_col = 0, 0
kms = 0
tunnels = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    line = input().split()
    matrix.append(line)
    if "T" in line:
        tunnels.append([i, line.index("T")])

while True:
    command = input()
    if command == "End":
        print(f"Racing car {num_car} DNF.")
        break
    else:
        new_row = directions[command][0] + car_row
        new_col = directions[command][1] + car_col
        if is_in_matrix(new_row, new_col):

            if matrix[new_row][new_col] == ".":
                kms += 10
                car_row, car_col = new_row, new_col

            elif matrix[new_row][new_col] == "T":
                kms += 30
                matrix[new_row][new_col] = "."
                car_row, car_col = new_row, new_col

                for t_row, t_col in tunnels:
                    if [t_row, t_col] != [new_row, new_col]:
                        car_row, car_col = t_row, t_col

                matrix[car_row][car_col] = "."

            elif matrix[new_row][new_col] == "F":
                matrix[new_row][new_col] = "."
                car_row, car_col = new_row, new_col
                kms += 10
                print(f"Racing car {num_car} finished the stage!")
                break

matrix[car_row][car_col] = "C"
print(f"Distance covered {kms} km.")
[print(''.join(el)) for el in matrix]
