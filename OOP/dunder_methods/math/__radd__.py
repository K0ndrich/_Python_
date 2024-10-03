# Магический Метод __radd__

# 10 + my_object
# Реалиает добавление + к числу нашего екзепляра класса

# Порядок Вызова Методов
# 10 + my_object -> __radd__ -> __add__


class MyClass:

    def __init__(self, value):

        self.value = value

    def __add__(self, other_value):

        return self.__class__(self.value + other_value)

    def __radd__(self, other_value):

        return self + other_value


my_object = MyClass(5)

my_object = 10 + my_object

my_object.value  # -> 15
