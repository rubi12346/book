class Book:
    def __init__(self,title,author,num_copies):
        self.title=title
        self.author=author
        self.num_copies=num_copies
    def __str__(self):
        return self.title
    
    