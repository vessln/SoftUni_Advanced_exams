def check_in_matrix(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(x) for x in input().split(",")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

cupboard = []
m_row, m_col = 0, 0
total_cheese = 0
eaten_cheese = 0

for i in range(rows):
    line = list(input())
    if "M" in line:
        m_row, m_col = i, line.index("M")

    if "C" in line:
        total_cheese += line.count("C")

    cupboard.append(line)

cupboard[m_row][m_col] = "*"

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break

    new_row = m_row + directions[command][0]
    new_col = m_col + directions[command][1]

    if not check_in_matrix(new_row, new_col):
        print("No more cheese for tonight!")
        break

    if cupboard[new_row][new_col] == "C":
        cupboard[new_row][new_col] = "*"
        m_row, m_col = new_row, new_col
        eaten_cheese += 1

        if eaten_cheese == total_cheese:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    if cupboard[new_row][new_col] == "T":
        cupboard[new_row][new_col] = "M"
        m_row, m_col = new_row, new_col
        print("Mouse is trapped!")
        break

    if cupboard[new_row][new_col] == "@":
        continue

    if cupboard[new_row][new_col] == "*":
        m_row, m_col = new_row, new_col

cupboard[m_row][m_col] = "M"

[print("".join(inner)) for inner in cupboard]