#Udělej generátor, kterému když zadám ["A","C","E","R"] a parametr 2 -> tak mi vygeneruje "AC", "CE" a "ER".
# Pokud zadám  ["A","C","E","R"] a parametr 3 -> tak mi vygeneruje "ACE", "CER"

def generuj(pismena:list[str], n: int):
    i = 0
    while i + n <= len(pismena):
        slovo = pismena[i]
        j = 1
        while j < n:
            slovo += pismena[i+j]
            j += 1
        yield slovo
        i += 1
for slovo in generuj(["A", "C", "E", "R"], 3):
    print(slovo)

print("RLE ")
#RLE (Run-length encoding, viz. https://en.wikipedia.org/wiki/Run-length_encoding). Řetězec AAAABBBCCDAA preveď na 4A3B2C2A.
#Tedy vždy počet daného písmene a poté to písmeno.
#Jiný příklad: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW se převede na 12W1B12W3B24W1B14W
#Dřív se pomocí tohoto algoritmu ukládaly obrázky.
def rle_gen(sekvence):
    if not sekvence:
        return
    count = 1
    for i in range(1, len(sekvence)):
        if sekvence[i] == sekvence[i - 1]:
            count += 1
        else:
            yield f"{count}{sekvence[i - 1]}"
            count = 1
    yield f"{count}{sekvence[-1]}"

rle_output = "".join(rle_gen("AAAABBBCCDAA"))
print(rle_output)