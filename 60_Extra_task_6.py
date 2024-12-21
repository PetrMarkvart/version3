Extra task 6:
Úloha: Systém pro správu knihovny
Vytvořte program, který umožňuje správu knihovny pomocí tříd a objektů.

Požadavky:
Třída Book
Atributy:
title (název knihy)
author (autor)
year (rok vydání)
is_borrowed (stav, jestli je kniha vypůjčená, výchozí hodnota je False)

Metody:
borrow(): Nastaví is_borrowed na True, pokud kniha není vypůjčená, jinak zobrazí zprávu, že je již vypůjčená.
return_book(): Nastaví is_borrowed na False.
Třída Library
Atributy:
books (seznam objektů typu Book)

Metody:
add_book(book): Přidá knihu do knihovny.
list_books(): Vypíše všechny knihy v knihovně s informací, zda jsou dostupné nebo vypůjčené.
find_book(title): Vyhledá knihu podle názvu a vrátí objekt Book (nebo None, pokud kniha neexistuje).
Hlavní program
Vytvořte několik knih a přidejte je do knihovny.
Implementujte menu, které umožní uživateli:
Zobrazit všechny knihy.
Vypůjčit knihu.
Vrátit knihu.
Přidat novou knihu.

'''
Příklad interakce:

1. Zobrazit všechny knihy
2. Vypůjčit knihu
3. Vrátit knihu
4. Přidat knihu
5. Konec

Vyberte akci: 1
1. Harry Potter (J.K. Rowling) - Dostupná
2. The Hobbit (J.R.R. Tolkien) - Vypůjčená
3. 1984 (George Orwell) - Dostupná
'''