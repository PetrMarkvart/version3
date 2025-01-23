from abc import ABC, abstractmethod

class Okno(ABC):

    @abstractmethod
    def tvar(self):
        print("Okno")

class Budova(Okno):
    pass

class Radiator(Budova):
    def tvar(self):
        print("Radiator")

class Svatlo(Radiator):
    pass

stul = Svatlo()
stul.tvar()