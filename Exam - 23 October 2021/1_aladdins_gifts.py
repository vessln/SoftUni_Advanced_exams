from collections import deque


def check_magic():
    if 100 <= values_sum <= 199:
        gifts["Gemstone"] += 1

    elif 200 <= values_sum <= 299:
        gifts["Porcelain Sculpture"] += 1

    elif 300 <= values_sum <= 399:
        gifts["Gold"] += 1

    elif 400 <= values_sum <= 499:
        gifts["Diamond Jewellery"] += 1


materials = deque([int(x) for x in input().split()])
magic_lvl = deque([int(x) for x in input().split()])

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and magic_lvl:
    first_magic = magic_lvl.popleft()
    last_material = materials.pop()

    values_sum = first_magic + last_material

    if values_sum < 100:
        if values_sum % 2 == 0:
            values_sum = (last_material * 2) + (first_magic * 3)
        elif values_sum % 2 != 0:
            values_sum = values_sum * 2

    if 100 <= values_sum <= 499:
        check_magic()

    if values_sum > 499:
        values_sum = values_sum / 2
        check_magic()


if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0)\
        or (gifts["Gold"] > 0 and gifts["Diamond Jewellery"]) > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in materials])}")

if magic_lvl:
    print(f"Magic left: {', '.join([str(el) for el in magic_lvl])}")

for el, count in sorted(gifts.items(), key=lambda x: x[0]):
    if count:
        print(f"{el}: {count}")
