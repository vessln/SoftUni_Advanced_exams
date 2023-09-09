from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    first_female = females.popleft()
    last_male = males.pop()

    if first_female <= 0 and last_male <= 0:
        continue
    elif first_female <= 0 and last_male > 0:
        males.append(last_male)
        continue
    elif last_male <= 0 and first_female > 0:
        females.appendleft(first_female)
        continue

    if first_female % 25 == 0 and len(females) > 0:
        females.popleft()
        males.append(last_male)
        continue

    if last_male % 25 == 0 and len(males) > 0:
        males.pop()
        females.appendleft(first_female)
        continue

    if first_female == last_male:
        matches += 1

    else:
        last_male -= 2
        males.append(last_male)

print(f"Matches: {matches}")
if males:
    males_list = list(males)
    print(f"Males left: {', '.join([str(x) for x in males_list[::-1]])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")