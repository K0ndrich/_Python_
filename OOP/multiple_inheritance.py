# Множественное Наследование

# Миксин (Mixin) -  это классы у которых нет данных(атрибутов), но есть методы. Основная ихняя функция добавить методов классу, но при етом его не изменять

# MRO (Method Resolution Order) - последовательность вызова методов в дочерних или родительских классах
# NoteBook -> Item -> Mixin -> Object

# В пример берем технику, которая продаеться в нашем магазине


class Item:

    # создает один товар нашего магазина
    def __init__(self, name, weight, price):
        print("- Create Item -")
        # метод __init__ вызываеться из класса Mixin, а не из главного класса object
        # Item -> Mixin
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    # выводит информацию о нашем товаре
    def print_info(self):
        print(f"{self.name}, {self.weight} , {self.price}")


class Mixin:

    # просто хранит id каждого товара в магазине
    ID = 0

    # создание id для товара
    # етот init для NoteBook не выполниться, если опередел первый init в Item
    # в миксинах нельзя использовать методы, где больше одного параметра self
    def __init__(self):
        print("- Create Mixin -")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: product was sold at 00:00 hours")

    def print_info(self):
        print(f"print_info from Mixin")


# дочерний класс, который описывает ноутбуки
# множественное наследование происходит слева на право, сначала наследуються атрибуты и методы Item, а потом уже от Mixin
# Mixin (Миксины) всегда прописываються в конце наследования для возможного переопредиления методов родительского класса Item
# НЕЛЬЗЯ ПИСАТЬ ВОТ ТАК -> class NoteBook(Mixin, Item):
# NoteBook -> Item -> Mixin -> object
class NoteBook(Item, Mixin):
    def print_info(self):
        Mixin.print_info(self)


# __mro__ возвращает последовательсность MRO наследования текущего дочернего класса от родительских
NoteBook.__mro__  # -> (<class '__main__.NoteBook'>, <class '__main__.Item'>, <class '__main__.Mixin'>, <class 'object'>)


my_notebook = NoteBook("Asus", 1.5, 3500)  # -> - Create Item - , - Create Mixin -


# метод вызываеться из класса Mixin
Mixin.print_info(my_notebook)  # -> print_info from Mixin


# метод также вызываеться из класса Mixin, но уже более по-простому
my_notebook.print_info()  # -> print_info from Mixin
