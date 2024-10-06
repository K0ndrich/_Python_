# Функции issubclass и isinstance

# Функция issubclass(my_other_class , my_parent_class) ->
# проверяет являеться первый класс дочерним(унаследованым) от указаного второго класса


# Функция isintance(my_object , my_class) ->
# проверяет являеться ли указаный обьект екзепляров класса, который мы указываем вторым


# MyClass1 -> object
class MyClass1:

    pass


# MyClass2 -> MyClass1 -> object
class MyClass2(MyClass1):
    pass


issubclass(MyClass1, object)  # -> True

issubclass(MyClass2, MyClass1)  # -> True

# тип данных int являеться дочерним классом от базового класса object
issubclass(int, object)  # -> True
issubclass(list, object)  # -> True


MyClass1.__name__  # -> MyClass1


my_object = MyClass1()

isinstance(my_object, MyClass1)  # -> True

isinstance(my_object, MyClass2)  # -> False


# -----   Розширяем Базовый Класс   -----------------------------------------------------------------------------------------------------------------------------------


# унаследуемся от базового класса list
class Vector(list):
    # self хранит ссылку на наш текущий список list
    def __str__(self):
        return " - ".join(map(str, self))


my_vector = Vector([1, 2, 3, 4, 5])

my_vector  # -> 1 - 2 - 3 - 4 - 5

type(my_vector)  # -> <class '__main__.Vector'>
