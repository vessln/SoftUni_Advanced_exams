from collections import deque


elves_energy = deque([int(x) for x in input().split()])
materials_box = deque([int(x) for x in input().split()])
idx, toys, energy = 0, 0, 0
not_enough_energy = False

while elves_energy and materials_box:
    first_elf = elves_energy.popleft()

    if first_elf < 5:
        continue

    idx += 1
    last_box = materials_box.pop()

    if idx % 3 == 0:
        if first_elf >= last_box * 2:
            toys += 2
            first_elf -= (last_box * 2)
            energy += last_box * 2
            elves_energy.append(first_elf + 1)
            if idx % 5 == 0:
                toys -= 2
                elves_energy[-1] -= 1
        else:
            not_enough_energy = True

    else:
        if first_elf >= last_box:
            toys += 1
            first_elf -= last_box
            energy += last_box
            elves_energy.append(first_elf + 1)
            if idx % 5 == 0:
                toys -= 1
                elves_energy[-1] -= 1
        else:
            not_enough_energy = True

    if not_enough_energy:
        elves_energy.append(first_elf * 2)
        materials_box.append(last_box)
        not_enough_energy = False


print(f"Toys: {toys}\nEnergy: {energy}")

if elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")

if materials_box:
    print(f"Boxes left: {', '.join([str(x) for x in materials_box])}")