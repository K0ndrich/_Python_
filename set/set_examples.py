# Примеры Работы с Множествами

# 1) Пример

# сортируем список от повторяемых значений
my_numbers = [1, 5, 6, 2, 4, 7, 8, 4, 3, 2, 1, 5, 8, 9, 2, 1]

# берем из списка только уникальные значения
unique_numbers = set(my_numbers)

unique_numbers  # -> {1, 2, 3, 4, 5, 6, 7, 8, 9}
type(unique_numbers)  # -> <class 'set'>

# переобразовываем множество обратно в список
my_numbers = list(unique_numbers)

my_numbers  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
type(my_numbers)  # -> <class 'list'>
