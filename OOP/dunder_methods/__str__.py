# Магический Метод __str__

# Метод __str__ вызываеться в момент использования функций print() или str() екзепляром класса
# Ето метод для отображения указаной информации для ПОЛЬЗОВАТЕЛЯ


class MyClass:

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Hello {self.name}"


my_object = MyClass("Kondrich")

print(my_object)  # -> Hello Kondrich

# при вызове в консоле
str(my_object)  # -> Hello Kondrich
