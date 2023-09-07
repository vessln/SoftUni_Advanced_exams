from collections import deque

quantities_food = deque([int(x) for x in input().split(", ")])
quantities_stamina = deque([int(x) for x in input().split(", ")])
peaks_lvl = deque([["Vihren", 80],
                   ["Kutelo", 90],
                   ["Banski Suhodol", 100],
                   ["Polezhan", 60],
                   ["Kamenitza", 70]],
                  )

conquered_peaks = []

while quantities_food and quantities_stamina and peaks_lvl:
    last_food = quantities_food.pop()
    first_stamina = quantities_stamina.popleft()

    food_stamina_sum = last_food + first_stamina

    info = peaks_lvl.popleft()
    peak, difficulty = info

    if food_stamina_sum >= difficulty:
        conquered_peaks.append(peak)
    else:
        peaks_lvl.appendleft(info)

if not peaks_lvl:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    print("\n".join(conquered_peaks))





