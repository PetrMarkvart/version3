def poklice(cena):
    print(f"Cena poklice je {cena}")

def trouba(cena):
    poklice(200)
    print(f"Cena trouby je {cena}")

def mycka(cena):
    trouba(3000)
    print(f"Cena myčky je {cena}")

mycka(40000)