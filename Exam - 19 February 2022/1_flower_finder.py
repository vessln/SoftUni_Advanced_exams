from collections import deque


flowers = {"rose": [], "tulip": [], "lotus": [], "daffodil": []}

vowels = deque(input().split())
consonants = deque(input().split())
found_word = False

while vowels and consonants and not found_word:
    first_v = vowels.popleft()
    last_c = consonants.pop()

    for char in [first_v, last_c]:
        for key, value in flowers.items():
            if char in key:
                value.append(char)

            if set(key) == set(value):
                found_word = True
                print(f"Word found: {key}")
                break

        if found_word:
            break

if not found_word:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")



