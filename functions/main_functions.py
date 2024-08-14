# Функции


# обьявление простой функции
def my_function():
    pass


# my_var1: int , my_var2: float просто подсказка для програмиста про желаемый тип данных передаваемых параметров
def my_function(my_var1: int, my_var2: float):
    pass


#  -> int подсказка для програмиста про желаемый тип возвращаемого значения функции
def my_function() -> int:
    pass


# return возвращает значения при успешном выполнении функции
def my_function():
    return 1


# pass пропускает выполнение работы функции
def my_function():
    pass  # -> <function my_fn at 0x000001D789D0A200>


# вызов функции и передача аргументов внутрь ее
my_function()  # -> 1
