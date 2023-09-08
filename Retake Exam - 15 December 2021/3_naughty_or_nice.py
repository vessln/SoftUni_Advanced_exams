def naughty_or_nice_list(*args, **kwargs):
    all_kids = {"Nice": [], "Naughty": [], "Not found": []}
    num_name = {}
    names = []
    santa_list, *commands = args

    for el in santa_list:
        if el[0] not in num_name.keys():
            num_name[el[0]] = []
        num_name[el[0]].append(el[1])

    for el in commands:
        number, kid_type = el.split("-")
        number = int(number)
        if number in num_name.keys():
            if len(num_name[number]) == 1:
                name_kid = num_name[number]
                all_kids[kid_type].append(*name_kid)
                del num_name[number]

    for k, v in num_name.items():
        names.extend(v)

    if kwargs:
        for key, value in kwargs.items():
            if names.count(key) == 1:
                all_kids[value].append(key)
                names.remove(key)

    if names:
        all_kids["Not found"].extend(names)

    result = ""
    for type_kid, name in all_kids.items():
        if name:
            result += f"{type_kid}: {', '.join(name)}\n"

    return result


# print(naughty_or_nice_list(
#     [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"),],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",))

# print(naughty_or_nice_list(
#     [(7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice", ))

# print(naughty_or_nice_list([(6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",))
