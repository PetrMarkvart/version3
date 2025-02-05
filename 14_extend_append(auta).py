# []
auta = ["Ford", "Audi", "Tesla"]
auta.append("Citroen")
print(auta)

print(f'mame {len(auta)} auta')
auta.append("Tatra")
print(f's Tatrou mame {len(auta)} auta')

cinska_auta = ["Volvo", "BYD"]
auta.extend(cinska_auta)
print(f'po pridani cinskych aut: {auta}')

auta.remove("Volvo")
print(f'po .pop mame: {auta}')



