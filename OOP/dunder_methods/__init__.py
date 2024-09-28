# Магический Метод __init__

# Метод __init__ вызываеться в момент создания екзеплара обьекта класса
# Метод __init__ являеться методом-конструктором


class MyClass:

    # self хранит ссылку на один текущий екзепляр обьекта класса
    def __init__(self, a, b):

        self  # -> <__main__.MyClass object at 0x000002758157C680>

        self.a = a
        self.b = b


my_object = MyClass(3, 5)
my_object.__dict__  # -> {'a': 3, 'b': 5}
