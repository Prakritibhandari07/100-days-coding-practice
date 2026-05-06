#Library Management Software in Python
#Question in video-64

class Library:
    def __init__(self):
        self.noofBooks=0
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)

    def showInfo(self):    
        print(f"The Library has {self.noBooks} books.The books are")
        for book in self.books:
            print(book)

l1=Library()
l1.addBook("Pranilcutie")
l1.addBook("harry Potter")
l1.showInfo()