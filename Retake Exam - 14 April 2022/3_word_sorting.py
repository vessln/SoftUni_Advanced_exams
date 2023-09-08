def words_sorting(*args):
    words_data = {}
    sum_all_values = 0

    for word in args:
        numbers_sum = sum([int(ord(x)) for x in word])
        words_data[word] = numbers_sum
        sum_all_values += numbers_sum
    # sum_values = sum(words_data.values())

    # even
    if sum_all_values % 2 == 0:
        sort_words = sorted(words_data.items(), key=lambda x: x[0])
    # odd
    else:
        sort_words = sorted(words_data.items(), key=lambda x: -x[1])

    result = ""
    for el in sort_words:
        result += f"{el[0]} - {el[1]}\n"

    return result


# print(words_sorting('escape', 'charm', 'mythology'))
#
# print(words_sorting('escape', 'charm', 'eye'))
#
# print(words_sorting('cacophony', 'accolade'))

