# Типы Полиморфизма

# Есть два типа Полиморфизма -> Ед-Хок Полиморфизм и Параметрический Полиморфизм

# Параметрический Полиморфизм - функции имеет одно выполнение(реализацию) для любого типа данных
# Ед-Хок Полиморфизм - функции имеет разные выполнения(реализации) для каждого отдельного типа данных

# -----   Параметрический Полиморфизм   -------------------------------------------------------------------------------------------------------------------


class A:

    def hello(self):
        print("Say hello class AAA")


class B:

    def hello(self):
        print("Say hello class BBB")


# выполение функции не зависит от типа данных агрумента, которая она принимает
def some(object_any_type):
    object_any_type.hello()


my_a = A()
my_b = B()

# передаем внутри функции езепляр класса
some(my_a)  # -> Say hello class AAA
some(my_b)  # -> Say hello class BBB

# передаем внутрь функции сам класс
some(A())  # -> Say hello class AAA
some(B())  # -> Say hello class BBB


# -----   Ед-Хок Полиморфизм   -------------------------------------------------------------------------------------------------------------------


# функция возвращает типы входящих аргумнетов
def to_type_value(value):

    if isinstance(value, int):
        return str(int)

    if isinstance(value, float):
        return str(int)

    if isinstance(value, str):
        return f"{value}"

    if isinstance(value, list):
        return "[" + ",".join(to_type_value(x) for x in value) + "]"


to_type_value(3)  # -> <class 'int'>

to_type_value(3.2)  # -> <class 'int'>

to_type_value("kondrich")  # -> kondrich

to_type_value([1, 2.3, "hello"])  # -> [<class 'int'> , <class 'int'> , hello]
