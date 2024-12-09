# []
auta = ["Ford", "Audi", "Tesla"]
print(auta)
auta.append("Citroen")
print(f'mame {len(auta)} auta')
auta.append("Tatra")
print(f'mame {len(auta)} auta')

cinska_auta = ["Volvo", "BYD"]
auta.extend(cinska_auta)
print(f'po pridani cinskych aut: {auta}')

