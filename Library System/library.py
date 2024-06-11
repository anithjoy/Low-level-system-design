from book import Book

class Library:
    def __init__(self,name):
        self.name = name
        self.books = [] # each book - title, author

    def addBook(self, book:Book):
        self.books.append(book)
        return self.books
    
    
    def searchBookByTitle(self, title):
        return [book for book in self.books if book.title == title]
    
    def searchBookByAuthor(self, author):
        return [book for book in self.books if book.author == author]
    
    def getAvailableBooks(self):
        return [book for book in self.books if not book.is_borrowed]

