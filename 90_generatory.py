#Ukázka generátoru sudých čísel

def gen_even(n):
    i = 0
    genereted_count = 0
    while genereted_count < n:
        print(f"Již jsme vygenerovali {genereted_count} čísel a i je {i}")
        if i % 2 == 0: #tzn.sudé číslo
            genereted_count += 1
            yield i
        i += 1

for sude_cislo in gen_even(5):
    print(f"Mám sudé číslo {sude_cislo}")


def gen_tri_jmena():
    yield "Zuzana"
    yield "Xenie"
    yield "Patrik"

for jmeno in gen_tri_jmena():
    print(jmeno)

#Úloha, udělejte generátor, který generuje následující sekvenci: 1, 2, 3, 5, 8, 13, 21, 34

def fib(kolik_cisel_celkem):
    kolik_jsme_vratili = 0
    a = 1
    b = 2
    while True:
        kolik_jsme_vratili += 1
        yield a
        soucet = a + b
        a = b
        b = soucet
        if kolik_jsme_vratili >= kolik_cisel_celkem:
            break

cisla = fib(8)
for cislo in cisla:
    print(cislo)

#řešení od Copilota
def custom_sequence_generator():
    sequence = [1, 2, 3, 5, 8, 13, 21, 34]
    for number in sequence:
        yield number

# Vytvoření instance generátoru
seq_gen = custom_sequence_generator()

# Výpis všech hodnot ze sekvence
for number in seq_gen:
    print







