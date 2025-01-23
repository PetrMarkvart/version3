#Task - udělat dekorátor, který vypíše, jak dlouho funkce trvala.
import time
def print_pred_a_za(fnc):

    def nahradni_fukce(*args, **kwargs):
        print("Jdeme vykonat funkci")
        start = time.time()  # zaznamená aktuální čas v době vykonání řádku
        navratova_hodnota = fnc(*args, **kwargs)
        end = time.time()  # zaznamená aktuální čas v době vykonání řádku
        print(f"Funkce vykonána během {end - start:.2f} sekund")
        return navratova_hodnota

    return nahradni_fukce

@print_pred_a_za
def zadej_cislo(cislo):
    vstup = int(input("Zadej číslo:"))
    print(f"Dvojnásobek čísla {vstup} je {vstup * cislo}")

zadej_cislo(5)