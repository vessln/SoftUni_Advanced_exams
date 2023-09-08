def in_matrix(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


def hit_D_or_T(row, col):
    up = int(matrix[0][col])
    down = int(matrix[6][col])
    left = int(matrix[row][0])
    right = int(matrix[row][6])
    points = up + down + left + right
    return points


SIZE = 7
first_pl_score, second_pl_score = 501, 501
turns_first, turns_second = 0, 0

player_1, player_2 = input().split(", ")
matrix = [input().split() for _ in range(SIZE)]

while True:
    # first turn:
    coordinates_first = input().strip("()").split(", ")
    row_1 = int(coordinates_first[0])
    col_1 = int(coordinates_first[1])
    turns_first += 1

    if in_matrix(row_1, col_1):
        if matrix[row_1][col_1] == "B":
            print(f"{player_1} won the game with {turns_first} throws!")
            break

        if matrix[row_1][col_1].isnumeric():
            first_pl_score -= int(matrix[row_1][col_1])

        elif matrix[row_1][col_1] == "D":
            deducted_point = (hit_D_or_T(row_1, col_1)) * 2
            first_pl_score -= deducted_point

        elif matrix[row_1][col_1] == "T":
            deducted_point = (hit_D_or_T(row_1, col_1)) * 3
            first_pl_score -= deducted_point

        if first_pl_score <= 0:
            print(f"{player_1} won the game with {turns_first} throws!")
            break

    # second turn:
    coordinates_second = input().strip("()").split(", ")
    row_2 = int(coordinates_second[0])
    col_2 = int(coordinates_second[1])
    turns_second += 1

    if in_matrix(row_2, col_2):
        if matrix[row_2][col_2] == "B":
            print(f"{player_2} won the game with {turns_second} throws!")
            break

        if matrix[row_2][col_2].isnumeric():
            second_pl_score -= int(matrix[row_2][col_2])

        elif matrix[row_2][col_2] == "D":
            deducted_point = (hit_D_or_T(row_2, col_2)) * 2
            second_pl_score -= deducted_point

        elif matrix[row_2][col_2] == "T":
            deducted_point = (hit_D_or_T(row_2, col_2)) * 3
            second_pl_score -= deducted_point

        if second_pl_score <= 0:
            print(f"{player_2} won the game with {turns_second} throws!")
            break