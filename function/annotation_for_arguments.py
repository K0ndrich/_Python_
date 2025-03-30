# Анотации Типов Агрументов, которые передаються в Функцию


# Простые типы данных
def my_function(a: int, b: float):
    pass

# Cписки
def my_function(numbers: list[int]):
    pass

# Списки с указанием типа значений внутри него
def my_function(numbers: list[int]):
    pass

# Кортежы
def my_function(numbers: tuple):
    pass

# Кортежы с указанием типа значений внутри него
def my_function(numbers: tuple[int]):
    pass

# Множества
def my_function(numbers: set[str]):
    pass

# Множества с указаныем типа значений внутри него
def my_function(numbers: set[str]):
    pass

# *ARGS - набор значений в виде кортежа
def my_function(*numbers: int)
    pass

# *KWARGS - набор значений в виде словаря
def send_data(**numbers: int)
    pass