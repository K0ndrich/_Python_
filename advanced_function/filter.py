# Продвинутая Функция Filter

# Ключ-Функция для filter() должна возвращать значение либо True либо False
# Может возвращать последователньость с другим количеством аргументов

# 1) -----   ПРИМЕР   ------------------------------------------------------------------------------------------------------------------------------


# создание ключ функции для filter()
def is_even(number: int):
    return number % 2 == 0  # -> True / False


my_numbers = [1, 4, 3, 2, 1, 6]

list(filter(is_even, my_numbers))  # -> [4, 2, 6]
type(filter(is_even, my_numbers))  # -> <class 'filter'>

# 2) -----   ПРИМЕР   ------------------------------------------------------------------------------------------------------------------------------\

my_people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 12},
    {"name": "Charlie", "age": 30},
]


# проверка на возраст
def is_adult(person: dict):
    return person["age"] > 18


list(
    filter(is_adult, my_people)
)  # -> [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
