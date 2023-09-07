def forecast(*args):
    data = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for name, weather in args:
        data[weather].append(name)

    result = ""
    for key, value in data.items():
        if key:
            for el in sorted(value):
                result += f"{el} - {key}\n"

    return result


# print(forecast(("Sofia", "Sunny"), ("London", "Cloudy"), ("New York", "Sunny")))
#
# print(forecast(("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"), ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"), ("Peru", "Sunny"),
#     ("Florence", "Cloudy"), ("Bourgas", "Sunny")))
#
# print(forecast(("Tokyo", "Rainy"), ("Sofia", "Rainy")))
