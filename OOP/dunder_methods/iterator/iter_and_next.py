# Магические Методы __iter__ и __next__


# класс для создания арифметической последовательности со значениями float
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):

        self.start = start
        self.stop = stop
        self.step = step

    # посзовлет итеритогваться по екземпляру текущего класса
    def __iter__(self):

        self.value = self.start - self.step
        # возвращаем езепляр текущего обьекта, каким являеться self
        return self

    # проходиться по всем значениям последовательности
    # позволяет вызывать функцию next()
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


my_numbers = FRange(0, 2, 0.5)
# my_numbers.__next__()  # -> 0.0
# next(my_numbers)  # -> 0.5
# my_numbers.__next__()  # -> 1.0

for x in my_numbers:
    x  # -> 0.0 , 0.5 , 1.0 , 1.5


# класс создает таблицу
class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):

        self.rows = rows
        # создаем один екземпляр предидущого класса FRange
        self.instance = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    # текущий next возвращает не значение, а последовательность значений(один row) в виде екзепляра класса FRange
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            # возвращает екзепляр класса FRange
            return iter(self.instance)
        else:
            raise StopIteration


my_table = FRange2D(0, 2, 0.5, 3)

for x in my_table:

    list(x)  # -> [0.0, 0.5, 1.0, 1.5]   [0.0, 0.5, 1.0, 1.5]   [0.0, 0.5, 1.0, 1.5]

for row in my_table:
    for x in row:
        x  # -> 0.0 , 0.5 , 1.0 , 1.5 , 0.0 , 0.5 , 1.0 , 1.5 , 0.0 , 0.5 , 1.0 , 1.5
