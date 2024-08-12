# Методы Списков


# .append(my_value) добавляет указаное значение в конец списка
my_list = ["apple", "bananas", "cherry"]
my_list.append("orange")  # -> ['apple', 'bananas', 'cherry', 'orange']

# .extend(my_list2) добавялет указаный список к первому списку в конец
my_list1 = [1, 2, 3]
my_list2 = [3, 4, 5]
my_list1.extend(my_list2)

# .insert(index , my_value) вставляем значение в список по индексу (добавление елемента, а не изменение существующего)
my_list = [1, 2, 3]
my_list.insert(2, 4)  # -> [1, 2, 4, 3]

# .remove(my_value) удаляет первый елемент в списке с указаным значением my_value
my_list = [1, 2, 3, 3, 4]
my_list.remove(3)  # -> [1, 2, 3, 4]

# .pop(index) удаляет елемент по индексу или последний
my_list = [1, 2, 3, 4]
my_list.pop()  # -> [1, 2, 3]
my_list.pop(1)  # -> [1, 3, 4]

# my_list(my_value) возвращает индекс первого елемента с указаным значением my_value
my_list = [1, 2, 3, 4]
my_list.index(3)  # -> 2

# .count(my_value) возвращает каличество елементов в списке с указаный значнием my_value
my_list = [1, 2, 3, 3, 3, 3]
my_list.count(3)  # -> 4

# .reverse() разворачивает список с конца на перед
my_list = [1, 2, 3, 4]
my_list.reverse()  # -> [4, 3, 2, 1]

# .clear() удалем все елементы списка
my_list = [1, 2, 3, 4]
my_list.clear()  # -> [ ]
