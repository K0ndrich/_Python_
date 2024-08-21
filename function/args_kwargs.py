# Аргументы - ARGS KWARGS - позволяеют передваться в функцию сразу множество обьектов

# ARGS принимает кортеж из аргументов
# KWARGS принимает словарь(ключ-значение) из аргументов


# простая функция принимает кортеж аргументов
def my_function(*args):  # -> <class 'tuple'>
    return args


my_function(1, 2, 3)  # -> (1, 2, 3)


def my_function(*args):
    summary = 0
    for my_value in args:
        summary += my_value
    return summary


my_function(1, 2, 3, 4, 5)  # -> 15

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
my_function(*my_list1, *my_list2)  # -> 30


# функция принимает словарь(ключ-значение) из аргументов
def my_function(**kwargs):  # -> <class 'dict'>
    return kwargs


my_function(name="Max", age=7)  # -> {'name': 'Max', 'age': 7}


# перебираем ключи и значения kwargs чезер цикл
def my_function(**kwargs):

    for my_key, my_value in kwargs.items():
        my_key


# розпаковываем словарь чтоб поместить в функцию
my_person = {"name": "Max", "age": 777}
my_function(**my_person)


# функция принимает любое количество аргументов
def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):

    x, y  # -> 1,2
    args  # -> (3, 4, 5)
    value  # -> 6
    kwargs  # -> {'name': 'Max', 'age': 777}


func_with_all_arguments(1, 2, 3, 4, 5, **my_person)
