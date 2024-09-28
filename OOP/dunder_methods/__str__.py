# Магический Метод __str__

# Метод __str__ вызываеться в момент использования функций print() или str()
# Ето метод для отображения указаной информации


class MyClass:
    def __str__(self):
        return f"Hello Kondrich"


my_object = MyClass()
# print(my_object)  # -> Hello Kondrich
