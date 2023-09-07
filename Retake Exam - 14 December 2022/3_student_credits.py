def students_credits(*args):
    courses_credits = {}
    sum_credits = 0

    for el in args:
        info = el.split("-")
        course = info[0]
        credits_ = float(info[1])
        max_points = float(info[2])
        D_points = float(info[3])
        if D_points != 0:
            D_credits = credits_ / (max_points / D_points)
        else:
            D_credits = 0

        sum_credits += D_credits

        if course not in courses_credits.keys():
            courses_credits[course] = 0
        courses_credits[course] += D_credits

    result = ""
    if sum_credits >= 240:
        result += f"Diyan gets a diploma with {sum_credits:.1f} credits."
    else:
        result += f"Diyan needs {240 - sum_credits:.1f} credits more for a diploma."

    for key, value in sorted(courses_credits.items(), key=lambda x: -x[1]):
        result += f"\n{key} - {value:.1f}"

    return result


# print(students_credits("Computer Science-12-300-250",
#     "Basic Algebra-15-400-200", "Algorithms-25-500-490"))
