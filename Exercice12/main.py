class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []
    # Ajouter les méthodes ici

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book_title == book.title:
                self.books.remove(book)
                break

    def borrow_book(self, book_title):
        if book_title in self.books:
            self.remove_book(book_title)
            self.borrow_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.borrow_books:
            self.borrow_books.remove(book_title)
            self.books.append(book_title)

    def available_books(self):
        return self.books

    def borrowed_books(self):
        return self.borrow_books

if __name__ == '__main__':
    book1 = Book("Un livre", "Moi", 1991)
    book2 = Book("DEUX livre", "Moi", 1991)
    book3 = Book("Trois livre", "Moi", 1991)

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.borrow_book("A lire")

    print("Livres dispo:", library.available_books())

    library.remove_book("Nul")

    print("---\nLivres dispo:", library.available_books())
    print("Livres emprunte:", library.borrowed_books())
