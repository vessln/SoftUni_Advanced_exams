from collections import deque

monsters_armor = deque([int(x) for x in input().split(",")])
soldiers_strike = deque([int(x) for x in input().split(",")])
killed_monsters = 0

while monsters_armor and soldiers_strike:
    first_armor = monsters_armor.popleft()
    last_strike = soldiers_strike.pop()

    if last_strike > first_armor:
        killed_monsters += 1
        last_strike -= first_armor

        if soldiers_strike:
            soldiers_strike[-1] += last_strike
        else:
            soldiers_strike.append(last_strike)

    elif last_strike == first_armor:
        killed_monsters += 1
        pass

    elif last_strike < first_armor:
        first_armor -= last_strike
        monsters_armor.append(first_armor)

    if not monsters_armor:
        print("All monsters have been killed!")

    if not soldiers_strike:
        print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")

