#Po vložení textu se vypíše, zdali je text pouze malými písmeny, či pouze velkými
#Nápověda: input(), text.lower(), text.upper(), operátor ==

vstup = input("Zadejte text:")
print(f"Je vstup pouze velkými písmeny? {vstup == vstup.upper()}")
print(f"Je to pouze malými? { vstup == vstup.lower()}")