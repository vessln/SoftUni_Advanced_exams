def start_spring(**kwargs):
    data = {}

    for k, v in kwargs.items():
        if v not in data.keys():
            data[v] = []
        data[v].append(k)

    result = ""
    for type_key, el_value in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{type_key}:\n"
        for el in sorted(el_value):
            result += f"-{el}\n"

    return result


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))
#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))

