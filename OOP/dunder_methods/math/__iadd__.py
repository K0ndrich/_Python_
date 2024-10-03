# Магический Метод __iadd__

# my_object += 10
# Реалиает добавление + к числу нашего екзепляра класса, но в укороченой форме записи
# При етом создаеться новый екзепляр нашего указаного класса

# Порядок Вызова Методов
# my_object += 10 -> __iadd__ -> __add__

class MyClass:

    def __init__(self, value):

        self.value = value

    def __add__(self, other_value):

        return self.__class__(self.value + other_value)

    def __iadd__(self, other_value):

        return self + other_value


my_object = MyClass(5)

my_object += 10

my_object.value  # -> 15
