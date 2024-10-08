# Типы Множеств
# Значения в множестве уникальные и не повторяються


# создание пустого множества
my_set = set()

# создание множества и сразу присваивание ему значений
my_set = {1, 4, 3, 2, 1, 2, 1, 1}  # -> {1, 2, 3, 4}

type(my_set)  # -> <class 'set'>

my_set = set()
for i in range(10):
    my_set.add(i)


my_set  # -> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# сравнения множеств
{1, 2, 3} == {1, 2, 3}  # -> True
{1, 2, 3} == {1, 2, 3, 4}  # -> False


# множество неупорядочений набор елементов, нельзя вызывать елементы множества по индексу
# my_set[i]  # -> ERROR


