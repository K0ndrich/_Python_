# Декоратор @property

# @property нужен чтоб не ломать логику работы обьектов класса
# @property позволяет взаемодействовать с атрибутами и методами класса только из вне и только тем которыми мы разрешим, которые public


class MyClass:

    def __init__(self, a):

        # __a режим доступа типа private
        # __a нельзя обращаться к таким отрибутам через обьект
        self.__a = a

    # def get_a(self):
    #     return self.__a

    # def set_a(self, a):

    #     self.__a = a
    # def del_a(self):
    #     pass

    # 1) ВАРИАНТ
    # нужен чтобы писать my_object.a вместо my_object.get_a()
    # теперь а становить обьектов property, а не просто переменной
    # a = property(get_a, set_a , del_a)

    # 2) ВАРИАНТ
    # a = property()
    # a = a.getter(get_a)
    # a = a.setter(set_a)
    # a = a.deleter(del_a)

    # 3) ВАРИАНТ
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @a.deleter
    def a(self):
        del self.__a
        # print("Delete was successful")


my_object = MyClass(7)

# геттер
my_object.a  # -> 7

# сеттер
my_object.a = 15
my_object.a  # -> 15


my_object.__dict__  # -> {'_MyClass__a': 15}

# делитер
del my_object.a  # -> Delete was successful

my_object.__dict__  # -> {}


# самостоятельно создаеться новый атрибут для обьекта класса
# етот атрибут b локальный типа public
my_object.b = 777
my_object.b  # -> 777
my_object.a = 15

my_object.__dict__  # -> {'b': 777, '_MyClass__a': 15}
