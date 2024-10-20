# Магический Метод __repr__

# Метод __repr__ создан для отображения информации об обьекте для разработчиков в режиме отладки в консоле
# Ето метод для отображения указаной информации для ПРОГРАМИСТА


class MyClass:

    name: str

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Hello {self.name}"


my_object = MyClass(name="Kondrich")

# если __str__ не определен, тогда будет визиваться метод __repr__
my_object  # -> Hello Kondrich
str(my_object)  # -> Hello Kondrich
repr(my_object)  # -> Hello Kondrich
