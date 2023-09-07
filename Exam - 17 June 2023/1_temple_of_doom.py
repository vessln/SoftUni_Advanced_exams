from collections import deque

tools_deque = deque([int(x) for x in input().split()])
substances_deque = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while tools_deque and substances_deque:
    first_tool = tools_deque.popleft()
    last_substance = substances_deque.pop()

    result = first_tool * last_substance

    if result in challenges:
        challenges.remove(result)

    else:
        tools_deque.append(first_tool + 1)
        if last_substance - 1 > 0:
            substances_deque.append(last_substance - 1)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if (not tools_deque or not substances_deque) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools_deque:
    print(f"Tools: {', '.join([str(x) for x in tools_deque])}")
if substances_deque:
    print(f"Substances: {', '.join([str(x) for x in substances_deque])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")