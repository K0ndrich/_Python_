# Области Видимости переменных в функциях


# показывает какие обьекты лежат в глобаной области видимости
globals().keys()  # -> dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__'])


# показывает какие обьекты лежат в локальной области видимости функции или цикла
locals().keys()  # -> dict_keys(['local_var'])


# -----   1) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------
# local_var нельзя вызвать вне области функции
def my_function():

    local_var = "1"
    locals().keys()
    print(local_var)  # -> 1


# my_function()
# local_var  # -> Error


# -----   2) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------
variable = "1"


def my_function():
    # variable значение изменять только внутри функции, вне функции значение остаеться прежним
    variable = "2"
    print(variable)


# my_function()  # -> 2
variable  # -> 1


# -----   3) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------

COMFORTABLE_TEMPERATURE = 25


def my_function(*, temperature: int):
    return COMFORTABLE_TEMPERATURE - temperature


my_function(temperature=30)  # -> -5


# -----   4) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------

my_var = 1


def my_function():
    # global указывает что будем использовать глобальную переменную
    global my_var
    my_var = 2


my_var  # -> 1
my_function()
my_var  # -> 2


# -----   5) Пример   -------------------------------------------------------------------------------------------------------------------------------------------------------
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
