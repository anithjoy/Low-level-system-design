from book import Book
class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def get_borrowed_books(self):
        return self.borrowed_books
    
    def add_borrowed_book(self, book:Book):
        self.borrowed_books.append(book)

    def remove_borrowed_book(self, book:Book):
        self.borrowed_books.remove(book)