from library import Library
from bookgyat import Book
library=Library()
book1=Book('the black dragon','rubi the king','50')
book2=Book('the white dragon','or the black guy','2')
library.add_book(book1)
library.add_book(book2)
library.display_inv()
library.save_inv()
