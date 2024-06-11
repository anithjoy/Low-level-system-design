from book import Book
from library import Library

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.borrowed_books = []

    # borrowed book-> list of books  
    def borrow_book(self,book:Book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.borrow()
            return True
        return False
    
    # return books -> list of books 
    def return_book(self,book:Book):
        if book.is_borrowed:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return True
        return False
    