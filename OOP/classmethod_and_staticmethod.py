# Декораторы Classmethod и Staticmethod

# Classmethod - метод класса, которй предназначен толкьо для вызова етого  метода внутри класса,
# екзепляр класса с сlassmethod взаемодействовать не может


# Staticmethod - метод класса, который не имеет доступа ни к атрибутам класса , ни к атрибутам екземпляра класса
# staticmethod можно вызывать только внутри класса, где был создан
# екзепляр класса с staticmethod взаемодействовать не может


class Vector:

    MIN_COORD = 0
    MAX_COORD = 100

    # cls ето ссылка на текущий класс Vector
    # создание метода класса
    @classmethod
    def validate(cls, argument) -> bool:
        return cls.MIN_COORD <= argument <= cls.MAX_COORD  # -> True / False

    def __init__(self, x, y):

        self.x = self.y = 0

        # Vector.validate()  == self.validate()
        # вызов classmethod внутри класса
        if self.validate(x) and self.validate(y):

            self.x = x
            self.y = y

            # вызов staticmethod внутри класса
            self.square(x, y   )  # -> 243

    # метод для получения значений кординат
    def get_cord(self) -> tuple:
        return self.x, self.y

    # создание статического метода
    @staticmethod
    def square(x, y):
        return x**y


my_object = Vector(3, 5)
my_object.get_cord()  # -> (3, 5)


# можно вызывать методы по другому, разницы нету
# внутрь передаем ссылку на новосозданый обьект
result = Vector.get_cord(my_object)
result  # -> (3, 5)


# передаваемые значения не прошли проверку в методе __init__
my_object2 = Vector(1, 400)
my_object2.get_cord()  # -> (0, 0)


# вызов classmethod метода вне класса
Vector.validate(3)  # -> True

# вызов staticmethod метода вне класса
Vector.square(3, 5)
