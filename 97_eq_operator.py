class Osoba:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other_object):
        return self.name == other_object.name

ruda1 = Osoba(30, "Ruda")
jura_novotny = Osoba(20, "Jura")
jura_stary = Osoba(30, "Jura")

if jura_novotny == jura_stary:
    print(f"{jura_novotny.name} je stejný jako {jura_stary.name}")
else:
    print(f"{jura_novotny.name} není stejný jako {jura_stary.name}")