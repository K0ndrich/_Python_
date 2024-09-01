# Декоратор @property

# @property нужен чтоб не ломать логику работы обьектов класса
# @property позволяет взаемодействовать с атрибутами и методами класса только из вне и только тем которыми мы разрешим, которые public


class MyClass:

    def __init__(self, a):

        # __a режим доступа типа private
        # __a нельзя обращаться к таким отрибутам через обьект
        self.__a = a

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

    # нужен чтобы писать my_object.a вместо my_object.get_a()
    a = property(get_a, set_a)


my_object = MyClass(7)


my_object.a  # -> 7


my_object.a = 10
my_object.a  # -> 10


my_object.__dict__  # -> {'_MyClass1__a': 10}


my_object.get_a()  # -> 10

my_object.set_a(15)
my_object.get_a()  # -> 15


# самостоятельно создаеться новый атрибут для обьекта класса
my_object.b = 777
my_object.b  # -> 777

# b являеться локальным(public) атрибутом обьекта класса
my_object.__dict__  # -> {'_MyClass__a': 15, 'b': 777}
