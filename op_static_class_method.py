class Pneumatika:

    @staticmethod
    def vypis_zakon():
        print("Zakon je &#@{}344/20 odstavec 8")

    @classmethod
    def vypis_funkce(cls):
        print(f"Vypisuji metody ze třídy {cls}")
        for funkce in dir(cls): #funkce dir vrátí list se všemi metodami
            if "__" not in funkce:
                print(funkce)

class SuperPneumatika(Pneumatika):
    def vymen_pneu(self):
        pass

Pneumatika.vypis_zakon()
SuperPneumatika.vypis_funkce()
Pneumatika.vypis_funkce()