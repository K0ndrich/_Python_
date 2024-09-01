# Полиморфизм Методов
# Когда одна функция(метод) может обрабатывать разные типы данных(екзпеляры классов)
# Методы Классов должны иметь одинаковые названия и переопределяться в классах наследниках


class MyClass1:

    def my_method(self):
        return "MyClass 1"

    def __str__(self):
        return f"Object for Class 1"


class MyClass2(MyClass1):

    def my_method(self):
        return "MyClass 2"

    def __str__(self):
        return f"Object for Class 2"


my_object1 = MyClass1()
my_object1.my_method()  # -> MyClass 1


my_object2 = MyClass2()
my_object2.my_method()  # -> MyClass 2


objects = [my_object1, my_object2]

for object in objects:
    object.my_method()  # -> MyClass 1 , MyClass 2
    print(object)  # -> Object for Class 1 , Object for Class 2
