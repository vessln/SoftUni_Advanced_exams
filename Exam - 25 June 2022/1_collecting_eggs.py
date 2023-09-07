from collections import deque


SIZE = 50
eggs_sizes = deque([int(x) for x in input().split(', ')])
papers_sizes = deque([int(x) for x in input().split(', ')])
boxes = 0

while eggs_sizes and papers_sizes:
    first_egg = eggs_sizes.popleft()

    if first_egg <= 0:
        pass

    elif first_egg == 13:
        papers_sizes[0], papers_sizes[-1] = papers_sizes[-1], papers_sizes[0]

    else:
        last_paper = papers_sizes.pop()
        if first_egg + last_paper <= SIZE:
            boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(i) for i in eggs_sizes)}")

if papers_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers_sizes)}")
