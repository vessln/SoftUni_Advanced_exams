from collections import deque

textiles = deque([int(x) for x in input().split()])
deque_meds = deque([int(x) for x in input().split()])

resources_items = {30: "Patch", 40: "Bandage", 100: "MedKit"}
items_create = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and deque_meds:
    first_textile = textiles.popleft()
    last_material = deque_meds.pop()

    create_value = first_textile + last_material

    if create_value in resources_items.keys():
        item = resources_items[create_value]
        items_create[item] += 1

    elif create_value > 100:
        item = resources_items[100]
        items_create[item] += 1
        remaining_resource = create_value - 100
        deque_meds[-1] += remaining_resource

    else:
        last_material += 10
        deque_meds.append(last_material)


if not textiles and not deque_meds:
    print("Textiles and medicaments are both empty.")

elif textiles and not deque_meds:
    print("Medicaments are empty.")

elif deque_meds and not textiles:
    print("Textiles are empty.")

if items_create:
    for item, amount in sorted(items_create.items(), key=lambda x: (-x[1], x[0])):
        if amount:
            print(f"{item} - {amount}")

if deque_meds:
    medics = list(str(x) for x in deque_meds)
    print(f"Medicaments left: {', '.join(medics[::-1])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")