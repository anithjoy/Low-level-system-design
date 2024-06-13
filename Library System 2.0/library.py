from book import Book
from member import Member

class Library:
    def __init__(self, name, max_Borrow = 2):
        self.name = name
        self.members = []
        self.books = []
        self.borrowed_books = []
        self.max_Borrow = max_Borrow

    def register_member(self, member: Member):
        self.members.append(member)

    def remove_member(self, member:Member):
        self.members.remove(member)

    def add_book(self,book:Book):
        self.books.append(book)

    def remove_book(self,book:Book):
        self.books.remove(book)


    #  search Feature
    def search_book_title(self, title:str):
        res =  [book for book in self.books if book.title == title]
        for result in res:
            print(f"{result.title};{result.author};{result.isbn};{result.copies}")
            
    
    def search_book_author(self, author:str):
        result =  [book for book in self.books if book.author == author]
        for res in result:
            print(f"{res.title};{res.author};{res.isbn};{res.copies}")
    
    def search_book_isbn(self, isbn:str):
        result = [book for book in self.books if book.isbn == isbn]
        for res in result:
            print(f"{res.title};{res.author};{res.isbn};{res.copies}")

    def search_member_name(self, name:str):
        result = [member for member in self.members if member.name == name]
        for res in result:
            print(f"{res.id};{res.name}")

    def search_member_id(self, id):
        result =  [member for member in self.members if member.id == id]
        for res in result:
            print(f"{res.id};{res.name}")
    
    def get_borrowed_books_by_member(self, member:Member):
        return member.borrowed_books if member.borrowed_books else None
    

    #  System Constraints
    def check_member_can_borrow(self, member:Member, book:Book):
        member_borrowed = member.borrowed_books
        if self.max_Borrow < len(member_borrowed):
            return False
        for b in member_borrowed:
            if b == book:
                return False
        return True

    # member borrow book feature
    def borrow_book (self, member:Member,book:Book):
        if self.check_member_can_borrow(member, book):
            if book.copies > 0:
                book.copies -= 1
                self.borrowed_books.append(book)
                member.add_borrowed_book(book)
                return True
        raise ValueError("No copies available")
    
    #  member return book feature
    def return_book (self, member:Member, book:Book):
        if book:
            book.add_copies(1)
            self.borrowed_books.remove(book)
            member.remove_borrowed_book(book)
            return True
        return False
    

    
    
