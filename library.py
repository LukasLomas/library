from book import Book
class library:
    def __init__ (self):
        self.books = []
        self.borrowed_count = 0
    def add_book (self, book):
        self.books.append(book)
    def borrow_book (self, title):
        for book in self.books: 
            if book.title == title:
                if book.borrow():
                    self.borrowed_count +=1 
                    return f"Successfully taken out: {title}"
                else: 
                    return f"{title} is already taken by somebody else"
        return f"{title} not found"
    def return_book (self, title):
        for book in self.books: 
            if book.title == title:
                if book.return_book ():
                    self.borrowed_count -=1
                    return f"Successfully brought back by the nerd who borrowed it: {title}"
                else:
                    return f"nobody has taken {title} because nobody wants it" 
        return f"we don't have {title} because it sucks"  