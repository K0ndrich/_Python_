class Cat:

    name: str

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Cat (name = {self.name})"

    def __str__(self):
        return f"It is my Cat {self.name}"


c = Cat(name="Barsik")

print(c)
print(str(c))
print(repr(c))
