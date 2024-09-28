# Магический Метод __call__

# Метод __call__ вызываеться при вызове екзепляра указаного класса

# Функторы - когда классы позволяют создавать екзепляри и ети екзепляри можно вызывать как функции()


# класс счетчик, который считает количество вызовов одного текущего екзепляра класса
class Counter:

    def __init__(self):
        self.__counter = 0

    # из чего состоит метод __call__ по-умолчанию в корнях python
    # def __call__(self, *args, **kwargs):
    #     obj = self.__new__(self, *args, **kwargs)
    #     self.__init__(obj, *args, **kwargs)
    #     return obj

    # теперь мы можем вызывать my_object()
    # step хранит шаг увеличение счетчика
    def __call__(self, step=1, *args, **kwargs):
        print("print __call__")
        self.__counter += step
        return self.__counter


my_object = Counter()

# вызываеться переопределенный нами магический метод  __call__
my_object()  # -> print __call__

my_object.__dict__  # -> {'_Counter__counter': 1}

my_object(6)

my_object.__dict__  # -> {'_Counter__counter': 7}

a = my_object()
a  # -> 8


# 1) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------


# Реализация Функции Замыкания через вызови екзепляров обьекта класса
# екзепляр класса удаляеть указаные символы перед и спосле после указаного слова
class StripChars:

    # chars харнит символы, которые будем удаляться в начале и в конце строки
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        # проверка являеться ли первое значение из кортежа args[0] строкой str G
        if not isinstance(args[0], str):
            raise TypeError("Argument must be string")

        # удаляем из строки указанные символы
        return args[0].strip(self.__chars)


# передаем символы которые будем удалять
my_object = StripChars("- ")

# передаем строку из которой будем удалять указаные ранее символы
my_object("   --- hello  --- ")  # -> hello


# 2) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------

# Реализация Декораторов Функций через вызов екзепляров обьекта класса


import math


# класс создан для вычесление производного от указаной функции в указаной точке x
class Derivate:

    # function хранит функцию, функционал которой будем расширять с помощью декторатора
    def __init__(self, function):
        self.__fn = function

    # x ето число от которого будем вычеслять производное числа
    # dx ето шаг изменение функции для вычесление производного от числа
    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


# функция вычесляет синус от указаного числа
def sinus_function(x):
    return math.sin(x)


# также можна указать декоратор для функции по стандартному
# @Derivate
# def sinus_function(x):
#     return math.sin(x)


# просто вызов функции sinus_function (не через класс Derivate)
sinus_function(math.pi / 4)  # -> 0.7071067811865476

# добавялет декоратор к функции, функция sinus_function начинает ссылаться на екзепляр класса Derivate
sinus_function = Derivate(sinus_function)

# ето вызов __call__ из класса Derivate
sinus_function(math.pi / 4)  # -> 0.7070714246681931 (значение изменилось)
