# Генераторы Списков , Множеств, Словарей , Генераторов


# 1) Генераторы Списков
my_list = [a for a in range(10) if a % 2 == 0]  # -> [0, 2, 4, 6, 8]
type(my_list)  # -> <class 'list'>

# генератор списка другой пример
my_list = [
    "yes" if my_num % 2 == 0 else "no" for my_num in range(5)
]  # -> ['yes', 'no', 'yes', 'no', 'yes']


# 2) Генераторы Множеств
my_set = {a for a in range(10) if a % 2 == 0}  # -> {0, 2, 4, 6, 8}
type(my_set)  # -> <class 'set'>


# 3) Генераторы Словарей
my_dict = {
    a: 10 for a in range(10) if a % 2 == 0
}  # -> {0: 10, 2: 10, 4: 10, 6: 10, 8: 10}
type(my_dict)  # -> <class 'dict'>

# генератор словаря другой пример
my_dict = {a: a**2 for a in range(5)}  # -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# 4) Генераторы Генераторов
# Генратор - ето обьект по которому можно итерироваться
my_generator = (a for a in range(10) if a % 2 == 0)  # -> 0 2 4 6 8
type(my_generator)  # -> <class 'generator'>

for i in my_generator:
    i  # -> # -> 0 2 4 6 8


