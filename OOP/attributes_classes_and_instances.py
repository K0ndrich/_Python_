# Атрибуты Класса и Екзепляров Класса


class MyClass:

    a: int = 3
    b: int = 5


my_object = MyClass()

# возвращает словарь со всеми атрибутами класса
MyClass.__dict__  # -> {'__module__': '__main__', '__init__': <function MyClass.__init__ at 0x0000015FFF5AD3A0>, '__str__': <function MyClass.__str__ at 0x0000015FFF5AD1C0>, 'my_method': <function MyClass.my_method at 0x0000015FFF5AD440>, '__dict__': <attribute '__dict__' of 'MyClass' objects> }


# возвращает словарь с локальными свойсвами перемеными екзепляра обьекта
my_object.__dict__  # -> {'a': 3, 'b': 5}


# возвращает MRO последовательность наследования текущего дочернего класса от родительских классов
# MyClass.__mro__  # -> (<class '__main__.MyClass'>, <class 'object'>)


# возвращает название класса по которому создался текущий обьект
# my_object.__class__  # -> <class '__main__.MyClass'>


# функция dir возвращает все методы указаного обьекта
# dir(my_object)  # -> ['__class__', '__delattr__', '__dict__','__eq__', '__format__', '__ge__', '__gt__']
