def shopping_cart(*args):
    card = {"Soup": [], "Pizza": [], "Dessert": []}

    for el in args:
        if el == "Stop":
            break

        meal, product = el[0], el[1]

        if meal == "Pizza":
            if product not in card["Pizza"] and len(card["Pizza"]) < 4:
                card["Pizza"].append(product)

        elif meal == "Soup":
            if product not in card["Soup"] and len(card["Soup"]) < 3:
                card["Soup"].append(product)

        elif meal == "Dessert":
            if product not in card["Dessert"] and len(card["Dessert"]) < 2:
                card["Dessert"].append(product)

    result = ""
    if len(card["Soup"]) == 0 and len(card["Pizza"]) == 0 and len(card["Dessert"]) == 0:
        result = "No products in the cart!"

    else:
        for key, value in sorted(card.items(), key=lambda x: (-len(x[1]), x[0])):
            result += f"{key}:\n"
            if value:
                for el in sorted(value):
                    result += f" - {el}\n"

    return result


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',))
#
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',))
#
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),))
