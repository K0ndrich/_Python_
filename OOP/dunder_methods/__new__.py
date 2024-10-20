# Магический Метод __new__

# Метод __new__ вызываеться перед созданеим екземпляра обьекта
# Содержит CLS - ссылку на текущий класс


class MyClass:

    # cls ссылаеться на текущий екзепляр класса, а именно на наш текущий класс MyClass
    # def __new__(cls):  # -> Error
    def __new__(cls, *args, **kwargs):

        str(cls)  # -> <class '__main__.MyClass'>

        # метод new должен возвращать ссылку на новосозданный екзепляр обьекта класса
        # super() -> Object
        return super().__new__(cls)  # -> Object.__new__(cls)


my_object = MyClass()
my_object.__dict__  # -> {}


# 1) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------


class A:

    def __new__(cls, *args, **kwargs):

        print("NEW")

        obj = super().__new__(cls, *args, **kwargs)
        return obj

    def __init__(self):

        print("INIT")

        self.some = 1


my_object = A()  # -> NEW , INIT

my_object.some  # -> 1
