# Декораторы Функций
# Декоратор - ето функция, которая принимает как аргумент другую функцию
# И добавляет к второй функции новый функционал


# -----   Декоратор Который Принимает Функцию БЕЗ Аргументов   ---------------------------------------------------------------------------------------------------


# создание декторатора
# внутрь принимает другую функцию без аргументов
def my_decorator(my_func):

    # функция обертка для второй функции
    def wrapper():

        print("BEFORE")

        my_func()  # -> HELLO

        print("AFTER")

    return wrapper


# добавление декоратора к функции
@my_decorator
def my_function():
    print("HELLO")


# my_function  # -> <function my_decorator.<locals>.wrapper at 0x000001F4EEA3D1C0>
# my_function()  # -> BEFORE , HELLO , AFTER


# добавление декоратора к функции по другому(не используеться)
# my_decorator(my_function)()  # -> BEFORE , HELLO , AFTER


# -----   Декоратор Который Принимает Функцию с Аргументами   ---------------------------------------------------------------------------------------------------


# декоратор который принимает функцию с аргументами
def my_decorator(my_func):

    # функция обертка для второй функции
    # *args, **kwargs ето аргументы которые принимает вторая функция my_func
    def wrapper(*args, **kwargs):

        print("BEFORE")

        my_func(*args, **kwargs)  # -> Kondrich

        print("AFTER")

    return wrapper


@my_decorator
def my_function(name):
    print(name)


# my_function("Kondrich")  # -> BEFORE , Kondrich, AFTER


# -----   Декоратор Который Принимает Функцию с Аргументами, Которая Возвращает Значение   ---------------------------------------------------------------------------------------------------


def my_decorator(my_func):

    def wrapper(*args, **kwargs):

        print("BEFORE")
        result = my_func(*args, **kwargs)

        print("AFTER")

        return result

    return wrapper


@my_decorator
def my_function(a, b):
    return a + b


# my_function(3, 5)  # -> BEFORE , AFTER

# my_sum = my_function(3, 5)  # -> BEFORE , AFTER
# my_sum  # -> 8

# -----   Декоратор Который Может Принимать Внутрь Себя Аргументы   ---------------------------------------------------------------------------------------------------


# декоратор указывает сколько раз будет повторяться функция, которую он оборачивает
# n - количество повторений функции, которую оборачиваем в декоратор
def repeat(n):
    def my_decorator(my_func):
        def wrapper(*args, **kwargs):
            print("BEFORE")
            # result хранит внутри себя результати выполнения всех функции
            result = []

            for x in range(n):
                r = my_func(*args, **kwargs)
                result.append(r)

            print("AFTER")
            return result

        return wrapper

    return my_decorator


@repeat(3)
def say_hello():
    print("HELLO")


say_hello()  # -> BEFORE , HELLO , HELLO , HELLO , AFTER
