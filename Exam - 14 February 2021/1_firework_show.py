from collections import deque


firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])
palm, willow, crossette = 0, 0, 0
success = False

while firework_effects and explosive_power:
    first_effect = firework_effects.popleft()
    last_power = explosive_power.pop()

    if first_effect <= 0 and last_power <= 0:
        continue

    elif first_effect <= 0 and last_power > 0:
        explosive_power.append(last_power)
        continue

    elif last_power <= 0 and first_effect > 0:
        firework_effects.appendleft(first_effect)
        continue

    mix_sum = first_effect + last_power

    if mix_sum % 3 == 0 and mix_sum % 5 != 0:
        palm += 1

    elif mix_sum % 5 == 0 and mix_sum % 3 != 0:
        willow += 1

    elif mix_sum % 3 == 0 and mix_sum % 5 == 0:
        crossette += 1

    else:
        first_effect -= 1
        firework_effects.append(first_effect)
        explosive_power.append(last_power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        success = True
        break

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

print(f"Palm Fireworks: {palm}\nWillow Fireworks: {willow}\nCrossette Fireworks: {crossette}")