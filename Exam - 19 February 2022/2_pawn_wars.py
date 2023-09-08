def check_diagonals(row, col, color):
    for el in diagonals[color]:
        new_r = row+el[0]
        new_c = col+el[1]

        if 0 <= new_r < SIZE and 0 <= new_c < SIZE:
            if color == "white":
                if matrix[new_r][new_c] == "b":
                    return new_r, new_c
            elif color == "black":
                if matrix[new_r][new_c] == "w":
                    return new_r, new_c


SIZE = 8
white_row, white_col = 0, 0
black_row, black_col = 0, 0
matrix = []
chessboard = []

for i in range(8, 0, -1):
    chess_row = []
    for j in range(97, 105):
        chess_row.append(f"{chr(j)}{i}")
    chessboard.append(chess_row)

diagonals = {
    "white": [(-1, -1), (-1, 1)],
    "black": [(1, 1), (1, -1)],
    }

for i in range(SIZE):
    line = input().split()
    matrix.append(line)

    if "w" in line:
        white_row, white_col = i, line.index("w")
    elif "b" in line:
        black_row, black_col = i, line.index("b")

while True:
    # white turn
    positions = check_diagonals(white_row, white_col, "white")
    if positions:
        new_row, new_col = positions[0], positions[1]
        print(f"Game over! White win, capture on {chessboard[new_row][new_col]}.")
        break

    matrix[white_row][white_col] = "-"
    white_row -= 1
    matrix[white_row][white_col] = "w"

    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {chessboard[white_row][white_col]}.")
        break

    # black_turn
    position = check_diagonals(black_row, black_col, "black")
    if position:
        new_row, new_col = position[0], position[1]
        print(f"Game over! Black win, capture on {chessboard[new_row][new_col]}.")
        break

    matrix[black_row][black_col] = "-"
    black_row += 1
    matrix[black_row][black_col] = "b"
    if black_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {chessboard[black_row][black_col]}.")
        break






