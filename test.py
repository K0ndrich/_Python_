class A:
    attr = 1

    def __init__(self):
        self.attr = 2


a = A()
print(a.attr)
print(A.__dict__)
