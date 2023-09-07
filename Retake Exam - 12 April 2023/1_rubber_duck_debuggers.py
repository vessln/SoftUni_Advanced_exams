from collections import deque


programmer_time = deque([int(x) for x in input().split()])
tasks_count = deque([int(x) for x in input().split()])
ducks_counting = {"Darth Vader Ducky": 0,
                  "Thor Ducky": 0,
                  "Big Blue Rubber Ducky": 0,
                  "Small Yellow Rubber Ducky": 0
                  }

while programmer_time and tasks_count:
    first_time = programmer_time.popleft()
    last_task = tasks_count.pop()

    calculated_time = first_time * last_task

    if 0 <= calculated_time <= 60:
        ducks_counting["Darth Vader Ducky"] += 1

    elif 61 <= calculated_time <= 120:
        ducks_counting["Thor Ducky"] += 1

    elif 121 <= calculated_time <= 180:
        ducks_counting["Big Blue Rubber Ducky"] += 1

    elif 181 <= calculated_time <= 240:
        ducks_counting["Small Yellow Rubber Ducky"] += 1

    elif calculated_time > 240:
        task_value = last_task - 2
        programmer_time.append(first_time)
        tasks_count.append(task_value)

if len(programmer_time) == 0 and len(tasks_count) == 0:
    print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for key, value in ducks_counting.items():
    print(f"{key}: {value}")









