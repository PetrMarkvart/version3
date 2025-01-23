class Zamestnanec:
    def __init__(self, jmeno, prijmeni, plat):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.plat = plat

    def zvysit_plat(self, o_kolik_zvysit):
        self.plat += o_kolik_zvysit

    def printit(self):
        print(f"Zaměstnanec {self.jmeno} prijmenim {self.prijmeni} má plat {self.plat}")

petr = Zamestnanec("Petr", "Novák", 60000)
petr.zvysit_plat(5000)
petr.printit() #Zaměstnanec Petr příjmením Novák má plat 65000 Kč

lenka = Zamestnanec("Lenka", "Nováková", 55000)
lenka.zvysit_plat(11000)
lenka.printit() #Zaměstnanec Lenka příjmením Nováková má plat 66000 Kč