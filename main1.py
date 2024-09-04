from book import Book
from library import library

book1 = Book("Why Apple is overpriced", "Lukas Lomas")
book2 = Book("Why pop music is terrible", "Lukas Lomas")
book3 = Book("Why we can't go to hell if we're already there", "Lukas Lomas")
book4 = Book("Why I refuse to be a part of some people's idiocracy", "Lukas Lomas")

library = library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

print (library.borrow_book ("Why Apple is overpriced"))
print (library.borrow_book ("Why Apple is overpriced"))
print (library.borrow_book ("Why Apple is overpriced"))
print (library.borrow_book ("Why Apple is overpriced"))
print (f"counter of times book has borrowed: {library.borrowed_count}")