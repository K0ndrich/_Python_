# Рекурсивная Функция - функция, которая вызывает саму себя

# Когда Стек Вызова Функции переполнен, тогда вылетает ошибка RecursionError


# -----   Неправильная Рекурсивная Функция   ------------------------------------------------------------------------------------------------------------------------------


def recursive_wrong(value):

    print(value)

    recursive_wrong(value + 1)


# recursive_wrong(1)  # -> Error


# -----   Правильная Рекурсивная Функция   ------------------------------------------------------------------------------------------------------------------------------


# правильная рекурсивная функция имеет условия для остановки
def recursive_correct(value):

    print(value)

    if value < 3:
        recursive_correct(value + 1)

    print(value)


# recursive_correct(1)  # -> 1 , 2 , 3 , 3 , 2 , 1


# -----   Вычесляем Факториал Числа   ------------------------------------------------------------------------------------------------------------------------------

# обозначение факториала числа
# !number = 1 * 2 * 3 * ... * number
# !5 = 1 * 2 * 3 * 4 * 5


# находи факториал числа с помощью РЕКУРСИИ
def find_factorial_with_recursive(number: int):

    # факториал от числа 1 равно 1
    if number <= 1:
        return 1

    else:
        result = number * find_factorial(number - 1)

    return result


find_factorial_with_recursive(5)  # -> 120


# НАХОДИМ ФОКТОРИАЛ ЧИСЛА С ПОМОЩЬЮ ЦИКЛА
def find_factorial_with_loop(number: int):
    value = 1
    while number >= 1:
        value = value * number
        number -= 1
    return value


find_factorial_with_loop(5)  # -> 120


# -----   Поиск Файла с Помощью Рекурсивной Функции   ------------------------------------------------------------------------------------------------------------------------------


F = {
    "C": {
        "Python39": ["python.exe", "python.ini"],
        "Program Files": {
            "Java": ["README.txt", "Welcome.html", "java.exe"],
            "MATLAB": ["matlab.bat", "matlab.exe", "mcc.exe"],
        },
        "Windows": {"System32": ["acledit.dll", "aclui.dll", "zipfldr.dll"]},
    }
}


# функция ищет файл в указаном пути
# path хранит в себе путь для поиска файла
# depth хранит в себе глубину обхода в path
def get_files(path, depth=0):

    # перебираем словарь path по ключам
    for f in path:

        print(" " * depth, f)

        # если обьект f который лежит внутри path являеться cловарем, тогда его нужно проходить дальше в глубь
        if type(path[f]) == dict:
            # дальше перебирает значения словаря, который лежит внутри
            get_files(path[f], depth + 1)
        else:
            # возвращает список файлов
            print(" " * (depth + 3), " ".join(path[f]))


# get_files(F)  # ->

#  C
#   Python39
#      python.exe python.ini
#   Program Files
#    Java
#       README.txt Welcome.html java.exe
#    MATLAB
#       matlab.bat matlab.exe mcc.exe
#   Windows
#    System32
#       acledit.dll aclui.dll zipfldr.dll
