from library import Library
from user import User
from book import Book

def main():
    # create a new 2 Library
    library1 = Library("Library1")

    # Add book to book
    book1 = Book("Harry Potter", "J.K. Rowling")
    book2 = Book("The Da Vinci Code", "Dan Brown")
    book3 = Book("The Alchemist", "Paulo Coelho")
    book4 = Book("The Kite Runner", "Khaled Hosseini")
    book5 = Book("The Catcher in the Rye", "J.D. Salinger")
    book6 = Book("The Running Grave", "J.K. Rowling")

    # add book to library
    print(f"books added {book1.title}",f"\t list of books",[book.title for book in library1.addBook(book1)])
    print(f"books added {book2.title}",f"\t list of books",[book.title for book in library1.addBook(book2)])
    print(f"books added {book3.title}",f"\t list of books",[book.title for book in library1.addBook(book3)])
    print(f"books added {book4.title}",f"\t list of books",[book.title for book in library1.addBook(book4)])
    print(f"books added {book5.title}",f"\t list of books",[book.title for book in library1.addBook(book5)])
    print(f"books added {book6.title}",f"\t list of books",[book.title for book in library1.addBook(book6)])
    print("\n")
    # Create 2 new user
    user1 = User("John",24)
    user2 = User("Cena",22)

    # Get all books from library1
    print("Library books", [book.title for book in library1.getAvailableBooks()])
    print("\n")

    # user1 borrow harrypotter from library1 -> True
    print(f"{user1.name} borrows {book4.title} ->",user1.borrow_book(book4))
    print(f"{user1.name} borrows {book2.title} ->",user1.borrow_book(book2))
    print( "Library books",[book.title for book in library1.getAvailableBooks()])
    print("\n")
    print(f"{user1.name} borrowed books till now->", [book.title for book in user1.borrowed_books])
    print("\n")

    #  User1 borrow harrypotter from library2 -> False
    print(f"{user1.name} trys to borrow same {book4.title} ->",user1.borrow_book(book4))
    print("\n")
    
    #  User returns to library
    print(f"{user1.name} returns {book2.title} ->",user1.return_book(book2))
    print( "Library books",[book.title for book in library1.getAvailableBooks()])
    print("\n")

    print(f"{user1.name} try to return same book {book2.title} ->",user1.return_book(book2))
    print("\n")

    # get all book by author
    print(f"{user1.name} wants to get all books by author name {book6.author} ->",[book.title for book in library1.searchBookByAuthor(book6.author)])
    print(f"{user1.name} wants to get all books by title name {book6.title} to know who is author->",[book.author for book in library1.searchBookByTitle(book6.title)])



    

if __name__ == '__main__':
    main()
