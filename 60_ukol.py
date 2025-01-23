class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
            print(f"Byla vypůjčena kniha {self.title}")
        else:
            print(f"Kniha {self.title} je již vypůjčena")

    def return_book(self):
        if self.is_borrowed == True:
            print(f"Byla vrácena kniha {self.title}")
        else:
            print(f"Kniha {self.title} nebyla vypůjčena")


babicka = Book("Babicka", "Nemcova", 1990)
babicka.borrow()
babicka.return_book()

class Library:
    def __init__(self):
        self.books : list[Book] = []

    def add_book(self, book : Book):
        self.books.append(Book)
