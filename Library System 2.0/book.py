class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.maxLimit = 5

    # number of copies to add or None
    def add_copies (self,num = None) -> bool:
        #  type cases
        if num < 0:
            return False
        
        # operation
        if self.maxLimit < self.copies+num :
            return False
        if num:
            self.copies += num
        else:
            self.copies += 1
        return True
    
    # number of copies to remove or None
    def remove_copies (self, num):
        #  type cases
        if num < 0:
            return False
        
        # operation 
        if self.copies <= 0 :
            return False
        if num:
            self.copies -= num
        else:
            self.copies -= 1
        return True
    



