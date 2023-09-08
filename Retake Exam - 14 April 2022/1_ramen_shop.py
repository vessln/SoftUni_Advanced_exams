from collections import deque


bowls_of_ramen = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while bowls_of_ramen and customers:
    first_client = customers.popleft()
    last_bowl = bowls_of_ramen.pop()

    if first_client == last_bowl:
        continue

    elif last_bowl > first_client:
        last_bowl -= first_client
        bowls_of_ramen.append(last_bowl)

    elif first_client > last_bowl:
        first_client -= last_bowl
        customers.appendleft(first_client)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")

elif not bowls_of_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join([str(x) for x in customers])}")
