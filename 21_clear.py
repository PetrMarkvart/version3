vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .clear() promažte vnořené listy tak, aby vsechny_jmena obsahovala pouze:
# ["Jura", [], "Božka", "Katka", []]
vsechny_jmena[1].clear()
vsechny_jmena[4].clear()

#   ŘÁDKY níže neupravujte
jmena = ["Jura", [], "Božka", "Katka", []]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")