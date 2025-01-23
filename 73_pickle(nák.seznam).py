'''
Task 73 - nákupní seznam
1. Pridať položku
2. Vypísať všetky položky
3. Zmazať položku
4. Upraviť položku
5. Uložiť zoznam do CSV
6. Načítať zoznam z CSV
7. Uložiť zoznam do pickle
8. Načítať zoznam z pickle
'''

class Polozka:
    def __init__(self, nazev):
        self.nazev = nazev

maslo = Polozka("maslo")
rum = Polozka("rum")
caj = Polozka("caj")

class Seznam:
    def __init__(self):
        self.polozky : list[Polozka] = []

    def pridat_polozku(self, polozka: Polozka):
        self.polozky.append(polozka)

    def vypsat_polozky(self):
        print("V seznamu je: ", end='')
        for polozka in self.polozky:
            print(f"{polozka.nazev}, ", end='')

    def smazat_polozku(self, polozka):
        self.polozky.remove(polozka)

    def upravit_polozku(self):
        pass

lidl = Seznam()
lidl.pridat_polozku(maslo)
lidl.pridat_polozku(rum)
lidl.vypsat_polozky()
lidl.smazat_polozku(rum)