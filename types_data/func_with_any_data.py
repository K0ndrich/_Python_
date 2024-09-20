# Как ведут себя функции с Изменяемыми и Неизменяемыми Типами Данных


# 1) -----   ПРИМЕР   ---------------------------------------------------------------------------------------------------------------------------------------------------


from copy import deepcopy


# Если внутрь функции передаем изменяемые обьекты, тогда изменяються сами обьекты, а не их копии
def func_with_computations(*, list: list[int]) -> None:

    list.clear()


my_list1 = [1, 2]

my_list2 = [1, 2]


# внутрь функции передаеться ссылка my_list и изменяеться сам обьект my_list, не его копия
func_with_computations(list=my_list1)

# внутрь функции передаеться копия обьекта, а не сам обьект
func_with_computations(list=deepcopy(my_list2))

my_list1  # -> []

my_list2  # -> [1, 2]


# 2) -----   ПРИМЕР   ---------------------------------------------------------------------------------------------------------------------------------------------------


# НЕЛЬЗЯ передавать в функцию изменяемые елементы с значениями по умолчанию как аргументы
# list будет добавлять новые значения и возвращать неправильный расширенный старый список
def append_in_list_bad(*, element: int, list=[]) -> list:

    list.append(element)
    return list


# правильная функция
# list будет хранить каждый раз новый список
def append_in_list_correct(*, element: int, list=None) -> list:

    if list is None:
        list = []
    list.append(element)
    return list


# append_in_list_bad
my_list = append_in_list_bad(element=1)
my_list  # -> [1]
another_list = append_in_list_bad(element=2)

my_list  # -> [1, 2]
another_list  # -> [1, 2]


# append_in_list_correct
my_list = append_in_list_correct(element=1)
my_list  # -> [1]
another_list = append_in_list_correct(element=2)

my_list  # -> [1]
another_list  # -> [2]


# 3) -----   ПРИМЕР   ---------------------------------------------------------------------------------------------------------------------------------------------------

# НЕЛЬЗЯ путать функции, которые изменяют существующую структуру изменяемого обьекта и функции которые возвращают изменяемый обьект

my_list = [3, 2, 1]

another_list = my_list.sort()

another_list  # -> None

another_list = sorted(my_list)

another_list  # -> [1, 2, 3]
