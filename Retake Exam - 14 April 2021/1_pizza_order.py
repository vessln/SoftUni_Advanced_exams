from collections import deque


orders_pizzas = deque([int(x) for x in input().split(", ")])
employees_capacity = deque([int(x) for x in input().split(", ")])
pizzas = 0

while orders_pizzas and employees_capacity:
    first_order = orders_pizzas.popleft()

    if first_order <= 0 or first_order > 10:
        continue

    last_capacity = employees_capacity.pop()

    if first_order <= last_capacity:
        pizzas += first_order

    elif first_order > last_capacity:
        remaining = first_order - last_capacity
        pizzas += last_capacity
        orders_pizzas.appendleft(remaining)


if not orders_pizzas:
    print(f"All orders are successfully completed!\nTotal pizzas made: {pizzas}")
    if employees_capacity:
        print(f"Employees: {', '.join([str(x) for x in employees_capacity])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders_pizzas])}")






