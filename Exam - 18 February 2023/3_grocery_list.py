def shop_from_grocery_list(budget, *args):
    grocery_list, *products_price = args

    for el in products_price:
        product = el[0]
        price = float(el[1])
        if budget < price:
            break

        if product in grocery_list:
            budget -= price
            grocery_list.remove(product)

    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."


# print(shop_from_grocery_list(100, ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8), ("chocolate", 30), ("tomato", 15.85), ("chips", 50), ("meat", 22.99)))
#
#
# print(shop_from_grocery_list(100, ["tomato", "cola"],
#     ("cola", 5.8), ("tomato", 10.0), ("tomato", 20.45)))