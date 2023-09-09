def get_magic_triangle(n):
    matrix = [[1], [1, 1]]

    for row_i in range(2, n):
        row_list = []

        for col_i in range(row_i+1):

            if col_i == 0 or col_i == row_i:
                row_list.append(1)

            else:
                el1 = matrix[row_i-1][col_i-1]
                el2 = matrix[row_i-1][col_i]
                row_list.append(el1+el2)

        matrix.append(row_list)

    return matrix


# print(get_magic_triangle(6))