def get_matrix(n, m, value):
#"""функция, создающая матрицу n строк х m столбцов,  и значаниями value"""

    matrix = []
#    n = 0
#   m = 0
#  value = 0

    for i in range(n):
        str = []
        matrix.append(str)
        for j in range(m):
            str.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

