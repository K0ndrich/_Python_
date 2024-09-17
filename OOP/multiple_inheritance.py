# Множественное Наследование
# Миксин (Mixin) -  это классы у которых нет данных(атрибутов), но есть методы. Основная ихняя функция добавить методов классу, но при етом его не изменять

# В пример берем технику, которая продаеться в нашем магазине


class Item:

    # создает один товар нашего магазина
    def __init__(self, name, weight, price):
        print("- Create Item -")
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
    def __init__(self):
        print("- Create Mixin -")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: product was sold at 00:00 hours")


# дочерний класс, который описывает ноутбуки
# множественное наследование происходит слева на право, сначала наследуються атрибуты и методы Item, а потом уже от Mixin
# Mixin (Миксины) всегда прописываються в конце наследования для возможного переопредиления методов родительского класса Item
class NoteBook(Item, Mixin):
    pass


my_notebook1 = NoteBook("Asus", 1.5, 3500)
my_notebook2 = NoteBook("Asus", 1.5, 3500)
my_notebook3 = NoteBook("Asus", 1.5, 3500)
# my_notebook.print_info()  # -> Asus, 1.5 , 3500
my_notebook3.save_sell_log()
