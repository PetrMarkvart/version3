class Zavada:
    def __init__(self, popis):
        self.popis = popis
    def __repr__(self):
        return f"Závada {self.popis}"

class LetajiciVec:
    def udelej_zvuk(self):
        print("Vrum")

class Helikoptery(LetajiciVec):
    def __init__(self, vyrobce):
        self.vyrobce = vyrobce
        self.zavady = []

    def __repr__(self):
        return f"Helikoptera {self.vyrobce}"

    def chyby_zavad(self):
        print(f"Helikoptera {self.vyrobce} má tyto závady")
        print(self.zavady)


airbus = Helikoptery("Airbus")
print(airbus)
defekt_1 = Zavada("porucha motoru")
airbus.zavady.append(defekt_1)
airbus.zavady.append(Zavada("Skla"))
airbus.chyby_zavad()
airbus.udelej_zvuk()