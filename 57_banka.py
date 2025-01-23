class Banka:
    def __init__(self, jmeno, zustatek):
        self.jmeno = jmeno
        self.zustatek = zustatek
        pass
       #třída Banka bude mít atribut jmeno a zustatek (počáteční zůstatek je 0)

    def vklad(self, castka):
        self.zustatek += castka
        #vložení částky k zůstatku
        pass

    def vyber(self, castka):
        self.zustatek -= castka
        #částka se odebere ze zůstatku
        pass

    def printit(self):
        print(f"V bance {self.jmeno} máme zustatek {self.zustatek} Kč.")

kb = Banka("kb", 0)
kb.vklad(20000)
kb.vyber(4000)
kb.printit()
#Vytvořte instanci třídy Banka

#Vložte 20000

#Vyberte 4000

#vyprintujte zůstatek a j