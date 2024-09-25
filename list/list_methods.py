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

# .sort() сортирует от меньшего к большему (reverse=True от большего к меньшему)
my_list = [3, 6, 4, 2, 1, 8, 2]
my_list.sort()  # -> [1, 2, 2, 3, 4, 6, 8]
my_list.sort(reverse=True)  # -> [8, 6, 4, 3, 2, 2, 1]

# .join(my_list) обединяет елементи списка, состоящего из букв в одну строку str и возвращает ету строку
my_list = ["h", "e", "l", "l", "o"]
my_string = "".join(my_list)  # -> hello
my_string = "-".join(my_list)  # -> h-e-l-l-o

# max(my_list)   min(my_list) возвращают максимальные и минимальные значение в указаной списке
my_list = [3, 6, 7, 3, 2, 1, 7, 9]
max(my_list)  # -> 9
min(my_list)  # -> 1

# sum(my_list) возвращает суму все значений списка
my_list = [3, 6, 7, 3, 2, 1, 7, 9]
sum(my_list)  # -> 38

# .clear() удалет все елементы списка
my_list = [1, 2, 3, 4]
my_list.clear()  # -> [ ]
