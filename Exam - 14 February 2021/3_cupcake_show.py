def stock_availability(*args):
    boxes = list(args[0])
    command = args[1]
    others = list(args[args.index(command)+1:])

    if command == "delivery":
        if others:
            for el in others:
                boxes.append(el)

    elif command == "sell":
        if not others:
            boxes.pop(0)
        else:
            for el in others:
                if str(el).isnumeric():
                    i = int(others[0])
                    boxes = boxes[i:]
                    break

                else:
                    count = boxes.count(el)
                    for _ in range(count):
                        boxes.remove(el)

    return boxes


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
