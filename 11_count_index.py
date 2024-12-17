text = "Pomoci specialniho prikazu s [] operatorem muzeme retezec precist od konce?"

#kolikrá se vyskytuje znak "s"
print(text.count('s'))

#na kterém indexu se vyskytuje znak "s"
print(text.index('s'))

#co se vyskytuje na indexu 7 po index 14
print(text[29:40])

#vyriznete text tak aby bylo vypsano slovo "operatorem"
print(f"slovo operatorem se vyskytuje na indexu: {text.index('operatorem')}")
print(text[29:42])

#z textu vypiste každy druhy znak
print(text[::2])

#text vypiste naopak
print(text[::-1])