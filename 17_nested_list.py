nested_list = [
    [1, 2, [3, 4, [5, 6, 5], 5], 5],
    [7, 8, [5, 9, 5,5]],
    [10, [11, 5, 6], 12]
]
#pomocí indexování zvolte pole [5, 6, 5]
#pozn. indexování je např. nested_list[2][0]
print(nested_list[0][2][2])
v = (nested_list[0][2][2])
print(v)
# pomocí .count zjistěte, kolikrát se vyskytuje 5 v tomto poli.
print(v.count(5))

vysledek = (v.count(5))

assert vysledek == 2, "Chybný výsledek"
print("Gratuluji, správný výsledek")
