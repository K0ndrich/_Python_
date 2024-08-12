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
