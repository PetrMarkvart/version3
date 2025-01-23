class Zakladni_trida:
    def __init__(self):
        self.name = "Nezadáno"

class Pokrocila_trida:
    def __init__(self, jmeno):
        self.name = jmeno

class Expert_trida:
    def __init__(self, jmeno):
        jmeno = f"Toto je jméno {jmeno}"
        jmeno = jmeno.upper()
        self.name = jmeno