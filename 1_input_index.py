slovo = input("napiste slovo: ")
print(f'napsal jste slovo: {slovo}')
print(f'napsane slovo ma: {len(slovo)} pismen')
promenna = input("napište jake pismeno hledate: ")
print(f'hledate pismeno: {promenna}')
print(f'hledane pismeno je v textu: {slovo.count(promenna)} krat')

print(f'toto je delka promenne: {len(promenna)}')

print(f'v textu je na indexu 1 znak: {slovo[2]}')

print(slovo[::-1])

print(len(slovo))