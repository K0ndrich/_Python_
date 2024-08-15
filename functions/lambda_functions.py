# Лямбда Функции (анонимные - безимянные - однострочные функции)


# (lambda my_argument1, my_argument2: my_argument1 + my_argument2) (my_value1, my_value2)
(lambda a, b: a + b)(3, 5)  # -> 8

# добавление действйи в функцию
(lambda a, b: a if a > b else b)(3, 5)  # -> 5
