# Функции Замыкания

# Замыкание - функция, которая находиться в другой внешней функции и работате с переменными из внешней функции
# Внешняя функция в конце своей работы возвращает функцию замыкания

# хронология по которой сылаються области видимости друг на друга
# f -> my_closure_function -> my_function -> global scope


def my_function(value):

    # создание функции замыкания
    def my_closure_function():
        print("Call closure function ")
        # функция замыкания взаемодествует с переменной из внешней функции
        print(f"Value from my_function() -> {value}")

    # вызов функции замикания
    return my_closure_function


my_function("kondrich")  # -> Nothing


# переменная f становить функцией
f = my_function("kondrich")

# вызов новосозданой функции
# f()  # -> Call closure function , Value from my_function() -> kondrich

a = my_function("hello")
# a()  # -> Call closure function  , Value from my_function() -> hello


# 1) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------


# функция счетчик, подсчитывет сколько раз одна нвосозданая функция вызвала текущую функцию counter
def counter(start=0):

    def step():
        nonlocal start
        start += 1
        return start

    return step


a = counter(10)
b = counter()

a(), a(), a()  # -> 11 , 12 ,  13
b(), b(), b()  # -> 1 , 2 , 3


# 2) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------


# функция, которая удаляет ненужные функции вначале и в конце строки
# strip_chars хранит символы, которые нужно будет удалять из строк
def strip_string(strip_chars=" "):
    # string хранит строку из которой будем удалять символы
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


str1 = strip_string()
str2 = strip_string("-")


str1("     hello      ")  # -> hello
str2("-----hello------")  # -> hello
