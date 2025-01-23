#Pomocí filter najděte rozlohy v rozmezí 800 až 10000
print("Pomocí filter najděte rozlohy v rozmezí 800 až 10000")
rozlohy = [88984, 345, 579875, 7594, 347985, 955, 545]
vyfiltrovane = print(list(filter(lambda rozloha: 800 <= rozloha <= 10000,rozlohy)))

#Pomocí reduce vynásobte všechny prvky
print("Pomocí reduce vynásobte všechny prvky")
prvky = [4,3,6,7]
from functools import reduce
prvky_nas = reduce(lambda x,y: x * y, prvky)
vysledek = (reduce(lambda x,y: x * y, prvky)) #ZDE doplnit místo 0
print(vysledek)

#Pomocí reduce najděte nejdelší řetězec v listu
print("Pomocí reduce najděte nejdelší řetězec v listu")
from functools import reduce

jazyky = ["JavaScript"]

def delsi(r1, r2):
    if len(r1) > len(r2):
        return r1
    else:
        return r2

nejdelsi =  reduce(delsi, jazyky)
nejdelsi2 =  reduce(lambda r1, r2: r1 if len(r1) > len(r2) else r2, jazyky)

print(nejdelsi)
print(nejdelsi2)