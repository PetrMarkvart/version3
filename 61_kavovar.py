class Kavovar:
    umisteni = "neznámé místo"
    mnozstvi_vody = 0

    def dopln_vodu(self, mnozstvi):
        self.mnozstvi_vody += mnozstvi
        print(f"Do kávovaru {self.umisteni} bylo doplněno {mnozstvi} ml vody. "
              f"Celkem je v něm nyní {self.mnozstvi_vody} ml vody.")

    def uvar_kavu(self):
        if self.mnozstvi_vody > 100:
            self.mnozstvi_vody -= 100
            print(f"Kávovar {self.umisteni} uvařil kávu. Zbývá {self.mnozstvi_vody} ml vody.")
        else:
            print(f"V kávovaru {self.umisteni} není dostatek vody!")

# Vytvoříme dvě instance kávovaru
kavovar_doma = Kavovar()
kavovar_v_kancelari = Kavovar()

# Nastavíme umístění pro oba kávovary
kavovar_doma.umisteni = "doma"
kavovar_v_kancelari.umisteni = "v kanceláři"

# Doplníme vodu do kávovaru v kanceláři
kavovar_v_kancelari.dopln_vodu(150)

# Zkusíme uvařit kávu v kávovaru doma
kavovar_doma.uvar_kavu()