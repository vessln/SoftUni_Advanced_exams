def moving(r, c, direct):
    r += directions[direction][0]
    c += directions[direction][1]
    if r >= rows:
        r = 0
    if r < 0:
        r = rows - 1
    if c >= cols:
        c = 0
    if c < 0:
        c = cols - 1

    return r, c


rows, cols = [int(x) for x in input().split(", ")]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

found_decors, found_gifts, found_cookies = 0, 0, 0
decors, gifts, cookies = 0, 0, 0
my_row, my_col = 0, 0
matrix = []
christmas = False

for i in range(rows):
    line = input().split()
    matrix.append(line)
    if "Y" in line:
        my_row, my_col = i, line.index("Y")
    if "D" in line:
        decors += line.count("D")
    if "C" in line:
        cookies += line.count("C")
    if "G" in line:
        gifts += line.count("G")

matrix[my_row][my_col] = "x"

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    direction = command[0]
    steps = int(command[1])
    for i in range(steps):
        my_row, my_col = moving(my_row, my_col, direction)
        if matrix[my_row][my_col] == "D":
            found_decors += 1
        elif matrix[my_row][my_col] == "C":
            found_cookies += 1
        elif matrix[my_row][my_col] == "G":
            found_gifts += 1
        matrix[my_row][my_col] = "x"

        if found_decors == decors and found_cookies == cookies and found_gifts == gifts:
            print("Merry Christmas!")
            christmas = True
            break

    if christmas:
        break

matrix[my_row][my_col] = "Y"
print("You've collected:")
print(f"- {found_decors} Christmas decorations")
print(f"- {found_gifts} Gifts")
print(f"- {found_cookies} Cookies")
[print(*inner_list) for inner_list in matrix]



