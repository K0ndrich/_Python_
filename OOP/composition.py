# Композиция

# Композиция - когда класс использует внутри себя екзепляры другого класса для розширения своего функционала


class Engine:

    def __init__(self, power):

        self.power = power

    def start(self):
        print(f"Engine start with {self.power} power")


class Car:

    # engine - ето екзепляр(обьект) класса Engine
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        # добавляем екзепляр класса Engine, как атрибут текущего класса Car
        self.engine = engine

    def start_cat(self):
        print(f"Starting car the {self.make} - {self.model}")

        self.engine.start()


my_engine = Engine(150)

my_car = Car("Toyota", "Corolla", my_engine)

my_car.start_cat()  # -> Starting car the Toyota - Corolla , Engine start with 150 power
