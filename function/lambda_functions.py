# Лямбда Функции (анонимные - безимянные - однострочные функции)


# (lambda my_argument1, my_argument2: my_argument1 + my_argument2) (my_value1, my_value2)
(lambda a, b: a + b)(3, 5)  # -> 8

# добавление действий в функцию
(lambda a, b: a if a > b else b)(3, 5)  # -> 5

# использование других функций внутри лямбда функции
(lambda a, b: abs(a) if a > b else float(b))(3, 5)  # -> 5.0


# присвоение лямбда функции внутрь переменной
my_lambda_function = lambda string: len(string)
my_lambda_function("kondrich")  # -> 8
type(my_lambda_function)  # -> <class 'function'>


# 1) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------

my_elements = ["banana", "apple", "orange", "pineaple"]

# сортировка елементов списка по длине от меньшего к большему
my_value = sorted(my_elements, key=lambda element: len(element))

my_value  # -> ['apple', 'banana', 'orange', 'pineaple']


# 2) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------

my_elements = ["banana", "apple", "orange", "pineaple"]

# возвращает самый длинный елемент
my_value = max(my_elements, key=lambda element: len(element))

my_value  # -> pineaple
