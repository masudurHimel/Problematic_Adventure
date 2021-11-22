class BaseClass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name


b = BaseClass(name="Something")
print(b.name)
b.name = "Another Thing"
print(b.name)

