def shopping_list(budget, **kwargs):
    result = ""

    if budget >= 100:
        basket = {}

        for product, values in kwargs.items():
            price = float(values[0])
            quantity = int(values[1])
            total_price = price * quantity

            if total_price <= budget:
                if product not in basket.keys():
                    basket[product] = 0
                basket[product] += total_price
                budget -= total_price

            if len(basket) == 5:
                break

        for key, value in basket.items():
            result += f"You bought {key} for {value:.2f} leva.\n"

    else:
        result = "You do not have enough budget."

    return result


# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))
#
# print(shopping_list(20, jeans=(19.99, 1),))
#
# print(shopping_list(104,
#         cola=(1.20, 2), candies=(0.25, 15),
#         bread=(1.80, 1), pie=(10.50, 5),
#         tomatoes=(4.20, 1), milk=(2.50, 2),
#         juice=(2, 3), eggs=(3, 1), ))
