slovo = input("napiste slovo: ")
print(f'napsal jste slovo: {slovo}')
print(f'napsane slovo ma: {len(slovo)} pismen')
promenna = input("napište jake pismeno hledate: ")
print(f'hledate pismeno: {promenna}')
print(f'hledane pismeno je na indexu: {slovo.count(promenna)}')

print(f'toto je delka promenne: {len(promenna)}')

print(f'v textu je na indexu 1:3:2 znaky: [text1:3:2]')

print(slovo[::-1])