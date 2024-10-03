# Магический Метод __add__

# my_object + 10
# Добавляет операцию добавления + значений к екзеплярам класса


class MyClass:

    def __init__(self, value):

        self.value = value

    # my_object + 100           можна
    # my_object1 + my_object2   не можна
    def __add__(self, other_value):

        # более не правильно
        # return MyClass(self.value + other_value)
        #
        # более правильно, можно будет заменять названия класса в коде
        return self.__class__(self.value + other_value)


my_object = MyClass(5)

# без определеного метода __add__()
# my_object += 3  # -> Error

# вместе с оперделенным методом __add__()
# ссылка обьекта присваиваться на новый екзепляр класса, который возвращает метод __add__
my_object += 3
my_object.value  # -> 8

my_object = my_object + 2
my_object.value  # -> 10
