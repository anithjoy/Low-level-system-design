from book import Book
from member import Member
from library import Library

# create library
library = Library("Aniths Library")

# Add book
Book1 = Book("Python", "Guido van Rossum","1234567890", 5)
Book2 = Book("Java", "James Gosling","1234567891", 2)

#  Add book to library
library.add_book(Book1)
library.add_book(Book2)

# Add member
Member1 = Member(1, "Anith")
Member2 = Member(2, "Sarath")

# Register Member to library
library.register_member(Member1)
library.register_member(Member2)

# borrow book from library
library.borrow_book(Member1, Book1)
library.borrow_book(Member1, Book2)

# return books to library
library.return_book(Member1, Book1)
library.return_book(Member1, Book2)

# search for books
library.search_book_title("Python")
library.search_book_author("Guido van Rossum")
library.search_book_isbn("1234567890")

#  search for members
library.search_member_name("Anith")
library.search_member_id(1)

