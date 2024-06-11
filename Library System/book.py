class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    #  if borrowed
    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True
    
    # if returned
    def _return(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    