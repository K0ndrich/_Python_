# Виды Копирования Словарей

# 1) -----   Простое Копирование   -------------------------------------------------------------------------------------------------------------------------------

my_dict = {"x": 1, "y": 2}
another_dict = my_dict

my_dict  # -> {'x': 1, 'y': 2}
another_dict  # -> {'x': 1, 'y': 2}

id(my_dict)  # -> 2384859359168  (одинаковые)
id(another_dict)  # -> 2384859359168  (одинаковые)

# значение ключа x сразу изменяеться у двух словарей
another_dict["x"] = 777

my_dict  # -> {'x': 777, 'y': 2}
another_dict  # -> {'x': 777, 'y': 2}


# 2) -----   Глубокое Копирование   -------------------------------------------------------------------------------------------------------------------------------

my_dict = {"x": 1, "y": 2}
another_dict = my_dict.copy()

my_dict  # -> {'x': 1, 'y': 2}
another_dict  # -> {'x': 1, 'y': 2}

id(my_dict)  # -> 2082499425984  (не одинаковые)
id(another_dict)  # -> 2036905864000  (не одинаковые)

# значение ключа x изменяеться только в указаном словаре another_dict, а значение в my_dict не изменяеться
another_dict["x"] = 777

my_dict  # -> {'x': 1, 'y': 2}
another_dict  # -> {'x': 777, 'y': 2}
