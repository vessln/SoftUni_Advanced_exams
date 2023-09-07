from collections import deque


caffeine_mgs = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])
MAX_CAFFEINE = 300
stamat_caffeine = 0

while caffeine_mgs and energy_drinks:
    last_mgs = caffeine_mgs.pop()
    first_drink = energy_drinks.popleft()

    calculation = last_mgs * first_drink

    if calculation + stamat_caffeine <= 300:
        stamat_caffeine += calculation
    else:
        energy_drinks.append(first_drink)
        stamat_caffeine -= 30 if stamat_caffeine >= 30 else 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")


