def accommodate_new_pets(capacity, max_weight, *args):
    pets_count_dict = {}
    is_accommodated = True

    for pet, weight in args:
        if capacity <= 0:
            is_accommodated = False
            break

        if weight <= max_weight:
            if pet not in pets_count_dict.keys():
                pets_count_dict[pet] = 0
            pets_count_dict[pet] += 1
            capacity -= 1

    result = []
    if not is_accommodated:
        result.append("You did not manage to accommodate all pets!")
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    for pet, count in sorted(pets_count_dict.items(), key=lambda x: x[0]):
        result.append(f"{pet}: {count}")

    return '\n'.join(result)


