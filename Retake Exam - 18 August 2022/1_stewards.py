from collections import deque


data_seats = set(input().split(", "))
numbers_one = deque([int(x) for x in input().split(", ")])
numbers_two = deque([int(x) for x in input().split(", ")])
rotations = 0
founded_matches = []

while True:
    if rotations == 10 or len(founded_matches) == 3:
        break

    first = numbers_one.popleft()
    last = numbers_two.pop()

    char = chr(first + last)
    comb_1, comb_2 = str(first)+char, str(last)+char

    combinations = set()
    combinations.add(comb_1)
    combinations.add(comb_2)
    seat_match = data_seats.intersection(combinations)
    rotations += 1

    if seat_match:
        seat = "".join(seat_match)
        if seat not in founded_matches:
            founded_matches.append(seat)

    else:
        numbers_one.append(first)
        numbers_two.appendleft(last)

print(f"Seat matches: {', '.join(founded_matches)}")
print(f"Rotations count: {rotations}")