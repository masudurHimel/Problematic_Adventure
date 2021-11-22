class TestClass:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        print("OKAY!!")
        return self.name + other

    def __del__(self):
        print("HERE")


t = TestClass('hello')
del t
