# Магический Метод __new__

# Метод __new__ вызываеться перед созданеим екземпляра обьекта класса


class MyClass:

    # cls ссылаеться на текущий екзепляр класса, а именно на наш текущий класс MyClass
    # def __new__(cls):  # -> Error
    def __new__(cls, *args, **kwargs):

        str(cls)  # -> <class '__main__.MyClass'>

        # метод new должен возвращать ссылку на новосозданный екзепляр обьекта класса
        # super() -> Object
        return super().__new__(cls)  # -> Object.__new__(cls)


my_object = MyClass()
print(my_object.__dict__)
