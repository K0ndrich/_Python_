# Транспонирование матрици, переворот матрици
# строки становятся столбцами, а столбци строками


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# как должны выглядеть транспонированая матрица
# transpone_matrix = [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9],
# ]

# 1) Пример трансопнирования матриции с помощью циклов

transpone_matrix = []

for i in range(len(matrix)):

    transpone_row = []

    len(matrix)  # -> 3

    i  # -> 0 , 1 , 2

    for row in matrix:

        row  # -> [1, 2, 3] / [4, 5, 6] / [7, 8, 9]  * 3
        transpone_row.append(row[i])

    transpone_row  # -> [1, 4, 7] / [2, 5, 8] / [3, 6, 9]

    transpone_matrix.append(transpone_row)

transpone_matrix  # ->
# [
# [1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]  ]


# 2) Пример трансопнирования матриции с помощью генераторов списков

# выполнение кода идет спрова на лево, основная часть находиться справа
transpone_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

# результат тотже
transpone_matrix  # ->
# [
# [1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]  ]
