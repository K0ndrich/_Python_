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
