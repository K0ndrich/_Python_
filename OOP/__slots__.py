# Колекция __slots__

# Указывает какие названия локальных атрибутов(свойства,методы) будут разрешены в екзеплеря нашего класса
# Ети ограничение налаживаться только на екзпляры класса, на сам класс ограничение не налаживаеться
# Атрибуты(свойства,методы), которые не разрешены в __slots__ нельзя будет создать

# Также использование __slots__ умньшаем размер памяти МБ для екзепляра класса


class MyClass:

    __slots__ = ("x", "y")

    MAX_COORD = 100

    def __init__(self, x, y):

        self.x = x
        self.y = y


my_object = MyClass(3, 5)

# нельзя создаться атрибут z, потому что он не указан в __slots__
# my_object.z = 777  # -> Error

# при использовании колекции __slots__, метод __dict__ не работает нужно переопределять
# my_object.__dict__  # -> Error

# значения екземпляров можно изменять
my_object.x = 7
my_object.y = 8
my_object.x, my_object.y  # -> 7 8

# значения НЕ локального атрибута класса, можно брать, но не можно изменять
my_object.MAX_COORD  # -> 100
# my_object.MAX_COORD = 30  # -> Error


# -----   Использование __slots__ вместе с Дикоратором @propetry   -----------------------------------------------------------------------------------------------------------------------------------


# колекция __slots__ НЕ налаживает никаких органичений на методы самого класса
# можем создавать сколько-угодно методов внутри самого класса
class MyPoint:

    __slots__ = ("x", "y", "__length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


my_object = MyPoint(5, 6)

# вызваеться метод @propetry length, а не свойство
my_object.length  # -> 7.8


# -----   Использование __slots__ при Наследовании Классов   -----------------------------------------------------------------------------------------------------------------------------------


class MyParentClass:

    __slots__ = ("x", "y", "__length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5


# колекция __slots__ не унаследуетсья дочерним классом, ето колекция там просто не работает
class MyDaughterClass(MyParentClass):
    pass


# если прописываеть пустой __slots__ в классе наследнике, тогда он там работает
class MyDaughterClass2(MyParentClass):
    # в текущий класс включаться все значения, которые были в родительском классе
    # __slots__ = ()
    #
    # добавляет к уже существующей колекции еще указаные значения
    __slots__ = "z", "k"

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z


my_object = MyDaughterClass(5, 6)

my_object.z = 7

# в классе наследике MyDaughterClass есть колекция __dict__
my_object.__dict__  # -> {'z': 7}

my_object.x  # -> 5
my_object.y  # -> 6


my_object2 = MyDaughterClass2(5, 6, 7)

my_object2.z  # -> 7

my_object2.k = 9
my_object2.k  # -> 9

# атрибут а не указан в колекции __slots__
# my_object2.a = 9  # -> Error

# в классе наследике MyDaughterClass2 есть колекция __dict__
# my_object2.__dict__  # -> Error
