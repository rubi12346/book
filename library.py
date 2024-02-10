
class Library:
    def __init__(self):
        self.bookava=[]
        self.bookunava=[]
    def add_book(self,book):
        self.bookava.append(book)
        print(f'sucsesfully added: {book.title}')
    def remove_book(self,book):
        if book in self.bookava:
            self.bookava.remove(book)
            print(f'removed sucsesfully nigger: {book.title}')
        else:
            print(f'the book is missing: {book.title}')
    def take(self,book):
        if book in self.bookava:
            self.bookava.remove(book)
            self.bookunava.append(book)
            print(f'taken sucsesfully nigger: {book.title}')
        else:
            print(f'the book is missing: {book.title}')
    def returnbook(self,book):
        if book in self.bookunava:
            self.bookava.append(book)
            self.bookunava.remove(book)
            print(f'sucsesfully returned: {book.title}')
        else:
            print(f'doesnt exist:{book.title}')
    def display_inv(self):
        for b in self.bookava:
            print(b)
    def save_inv(self):
        with open('kobez.txt','r') as file:
            for book in self.bookava:
                file.write(f'{book.title}|{book.author}|{book.num_copies}\n')






    
        
   

        

         
        

        
        



