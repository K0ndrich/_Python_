# Магический Метод __abs__

# Позволяет применять функцию abs() к екзеплярам класса
# Функция abs() вычесляет модуль от указаного числа


class MyClass:

    def __init__(self, *args):

        # __coords хранит список из значения координат, которые передавались при создании уекзепляра обьекта
        self.__coords = args

    def __abs__(self):
        return list(map(abs, self.__coords))


my_object = MyClass(-1, -2)

abs(my_object)  # -> [1, 2]
type(abs(my_object))  # -> <class 'list'>
