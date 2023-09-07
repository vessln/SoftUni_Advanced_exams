def gather_credits(*args):
    my_credits = 0
    passed_courses = []
    total_credits = args[0]
    course_credits_dict = {}

    for el in args[1:]:
        course_credits_dict[el[0]] = el[1]

    for name, crd in course_credits_dict.items():
        if my_credits < total_credits:
            if name not in passed_courses:
                my_credits += crd
                passed_courses.append(name)

        if my_credits >= total_credits:
            break

    if my_credits >= total_credits:
        return f"Enrollment finished! Maximum credits: {my_credits}.\n" \
                   f"Courses: {', '.join(sorted(passed_courses))}"

    else:
        return f"You need to enroll in more courses! You have to gather {total_credits-my_credits} credits more."
