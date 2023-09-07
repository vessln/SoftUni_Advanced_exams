def unpack_coordinates(coordinates):
    coords = coordinates.strip("()").split(", ")
    row, col = int(coords[0]), int(coords[1])
    return row, col


first_player, second_player = input().split(", ")
SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]
first_player_rest, second_player_rest = False, False

while True:
    # first:
    first_coordinates = input()

    if not first_player_rest:
        new_row, new_col = unpack_coordinates(first_coordinates)

        if matrix[new_row][new_col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break

        elif matrix[new_row][new_col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break

        elif matrix[new_row][new_col] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_rest = True

    else:
        first_player_rest = False

    # second:
    second_coordinates = input()
    if not second_player_rest:
        new_row, new_col = unpack_coordinates(second_coordinates)

        if matrix[new_row][new_col] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break

        elif matrix[new_row][new_col] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break

        elif matrix[new_row][new_col] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_rest = True

    else:
        second_player_rest = False


