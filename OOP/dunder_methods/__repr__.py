# Магический Метод __repr__

# Метод __repr__ создан для отображения информации об обьекте для разработчиков в режиме отладки в консоле
# Ето метод для отображения указаной информации


class MyClass:

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"Class Name : {self.__class__} -> {self.name} "


my_object = MyClass("Kondrich")

my_object  # -> Class Name : <class '__main__.MyClass'> -> Kondrich

str(my_object)
