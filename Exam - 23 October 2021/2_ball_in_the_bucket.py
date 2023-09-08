def in_matrix(r_, c_):
    return 0 <= r_ < SIZE and 0 <= c_ < SIZE


def sum_column(c):
    point = 0
    for x in range(SIZE):
        el = matrix[x][c]
        if el.isdigit():
            point += int(el)
    return point


SIZE = 6
my_row, my_col = 0, 0
points = 0

matrix = [input().split() for _ in range(SIZE)]

for i in range(3):
    coordinates = input().strip("()").split(", ")
    row, col = int(coordinates[0]), int(coordinates[1])

    if in_matrix(row, col):
        if matrix[row][col] == "B":
            matrix[row][col] = "0"
            points += sum_column(col)

if points < 100:
    print(f"Sorry! You need {100-points} points more to win a prize.")

elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")

elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")

elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")




