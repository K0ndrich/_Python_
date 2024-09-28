# Магический Метод __call__

# Метод __call__ вызываеться при вызове екзепляра указаного класса

# Функторы - когда классы позволяют создавать екзепляри и ети екзепляри можно вызывать как функции()


# класс счетчик, который считает количество вызовов одного текущего екзепляра класса
class Counter:

    def __init__(self):
        self.__counter = 0

    # из чего состоит метод __call__ по-умолчанию в корнях python
    # def __call__(self, *args, **kwargs):
    #     obj = self.__new__(self, *args, **kwargs)
    #     self.__init__(obj, *args, **kwargs)
    #     return obj

    # теперь мы можем вызывать my_object()
    # step хранит шаг увеличение счетчика
    def __call__(self, step=1, *args, **kwargs):
        print("print __call__")
        self.__counter += step
        return self.__counter


my_object = Counter()

# вызываеться переопределенный нами магический метод  __call__
my_object()  # -> print __call__

my_object.__dict__  # -> {'_Counter__counter': 1}

my_object(6)

my_object.__dict__  # -> {'_Counter__counter': 7}

a = my_object()
a  # -> 8


# 1) -----   ПРИМЕР   -------------------------------------------------------------------------------------------------------------------


# реализация функции замыкания через вызови екзепляров обьекта класса
# екзепляр класса удаляеть указаные символы перед и спосле после указаного слова
class StripChars:

    # chars харнит символы, которые будем удаляться в начале и в конце строки
    def __init__(self, chars):
        self.__counter = 0
        self.chars = chars

    def __call__(self, *args, **kwargs):
        # проверка являеться ли первое значение из кортежа args[0] строкой str G
        if not isinstance(args[0], str):
            raise TypeError("Argument must be string")

        # удаляем из строки указанные символы
        return args[0].strip(self.chars)


# передаем символы которые будем удалять
my_object = StripChars("- ")

# передаем строку из которой будем удалять указаные ранее символы
my_object("   --- hello  --- ")  # -> hello
