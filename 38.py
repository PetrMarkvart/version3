cislo = 1
while cislo < 5:
    print(cislo)
    cislo += 1
print(f"Hotovo, číslo je {cislo}")
#vykoná se řádek 1 -> cislo bude 1
#vykoná se porovnání na řádku 2. 1 < 5, takže se začne vykonávat tělo while
#vykoná se řádek 3 -> vypíše se 1
#vykoná se řádek 4 -> cislo bude 2
#vykoná se porovnání na řádku 2. 2 < 5, takže se začne vykonávat tělo while
#vykoná se řádek 3 -> vypíše se 2
#vykoná se řádek 4 -> cislo bude 3
#vykoná se porovnání na řádku 2. 3 < 5, takže se začne vykonávat tělo while
#vykoná se řádek 3 -> vypíše se 3
#vykoná se řádek 4 -> cislo bude 4
#vykoná se porovnání na řádku 2. 4 < 5, takže se začne vykonávat tělo while
#vykoná se řádek 3 -> vypíše se 4
#vykoná se řádek 4 -> cislo bude 5
#vykoná se porovnání na řádku 2. 5 < 5 NEPLATÍ, takže se skočí na řádek 5
#vykoná se řádek 5 - vypíše se Hotovo, číslo je 5

'''
n = 0
soucet_lichych_cisel = 0
while n < 7:
    n += 1
    if n % 2 == 0:
        print("N je sudé")
        continue
    print(f"Hodnota N je {n}")
    soucet_lichych_cisel += n
print(soucet_lichych_cisel)
'''

cisla = [3, 4, 5, 20, 30]
for cislo in cisla:
    print(cislo*2)