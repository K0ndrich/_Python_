# Абстракный Класс - нельзя создат екзепляр такого класса, служит только для создания дочерних классов по своему подобию

from abc import ABC, abstractmethod


# создание абстрактоного класса
# класс становиться абстаркным только если в нем есть хотябы один абстрактный метод
class Animal(ABC):

    @abstractmethod
    def say_something(self):
        pass


# класс наследник от абстрактного класса
class Cat(Animal):

    # в дочернем классе нужно переопределять методы из абастрактоного класса
    # название переопределеных перетодов должни бить такие же как и в абстрактном классе
    def say_something(self):
        return "Hello"


a = Cat()
a.say_something()  # -> Hello
