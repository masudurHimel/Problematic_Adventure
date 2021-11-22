from abc import ABC, abstractmethod


class M(ABC):
    @abstractmethod
    def spd(self):
        print('spd')

    @abstractmethod
    def pdb(self):
        print('pdb')


class Temp(M):

    def spd(self):
        pass

    def pdb(self):
        pass

    def __init__(self):
        pass

    @staticmethod
    def rtr():
        return "Oka"


a = Temp()
print(a.rtr())
