
#Zadání:
#Napiš program, který požádá uživatele o zadání čísla odpovídající přijmu firmy:

#pokud je číslo kladné, tak se vypíše "Firma je v zisku"
#pokud je číslo nula, tak se vypíše "Firma je na nule"
#pokud je číslo záporné, tak se vypíše "Brzo bude krach"

příjem = int(input("napiš příjem: "))
if příjem > 0:
    print("Firma je v zisku")
if příjem == 0:
    print("Firma je na nule")
if příjem < 0:
    print("Jdeš do kopru")
