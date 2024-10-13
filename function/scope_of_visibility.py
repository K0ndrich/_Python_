# Области Видимости переменных в функциях
# LEGB - Local, Enclosing, Global , Build-in - Правило по которому работает простравноство имен в Python

# показывает какие обьекты лежат в глобаной области видимости
globals().keys()  # -> dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__'])


# показывает какие обьекты лежат в локальной области видимости функции или цикла
locals().keys()  # -> dict_keys(['local_var'])


# -----   LEGB   -------------------------------------------------------------------------------------------------------------------------------------------------------

# глобальная область видимости
my_str = "global"


def outher():
    # внутрення облатсть видимости
    # my_str = "enclosing"

    def inner():
        # локальная область видимости
        # my_str = "local"
        print(my_str)

    inner()


# outher()  # -> local      ,если переменная my_str есть  внутри inner()
# outher()  # -> enclosing  ,если переменной my_str нету внутри inner()
# outher()  # -> global     ,если переменной my_str нету внутри функции outher()


# -----   1) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------
# local_var нельзя вызвать вне области функции
def my_function():

    local_var = "1"
    locals().keys()
    print(local_var)  # -> 1


# my_function()
# local_var  # -> Error


# -----   2) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------


def my_function(start=0):

    # ето функция замыкания
    def my_closure_function():

        # nonlocal указывает что будем работать с переменной из внешней функции, переменная не из глобальной функции
        nonlocal start

        start += 1
        return start

    # возвращает функцию замыкания
    return my_closure_function


a = my_function(10)

a(), a(), a()  # -> 11 , 12 , 13


# -----   3) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------
variable = "1"


def my_function():
    # variable значение изменяеться только внутри функции, вне функции значение остаеться прежним
    variable = "2"
    print(variable)


# my_function()  # -> 2
variable  # -> 1


# -----   4) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------

COMFORTABLE_TEMPERATURE = 25


def my_function(*, temperature: int):
    return COMFORTABLE_TEMPERATURE - temperature


my_function(temperature=30)  # -> -5


# -----   5) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------

my_var = 1


def my_function():
    # global указывает что будем использовать глобальную переменную
    global my_var
    my_var = 2


my_var  # -> 1
my_function()
my_var  # -> 2


# -----   6) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------
DEFAULT_LEVEL_EXPERIENCE = 200


# функция определяет нужно ли повишать уровень персонажа в игре
def is_level_up(*, current_experience: int, ganied_experience: int):
    total_experience = current_experience + ganied_experience
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        # level_up = True повишаем левер пресонажа
        level_up = True

    return level_up


is_level_up(current_experience=150, ganied_experience=30)  # -> False
is_level_up(current_experience=150, ganied_experience=70)  # -> True
