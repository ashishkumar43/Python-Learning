 #Write a library class with no_of_books and books with 2 instance variavles.Write a program to create a library from this library class and show how you can print all books and a book and get the number of books using different methods. Show that your program doesnot persist the books after the program is stopped
 
class library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
        
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
        
    def showInfo(self):
        print("The Library has {self.noBooks} books. The Books are ")
        for book in self.books:
            print(book)
        
l1=library()
l1.addBook("Atomic Habbit1")
l1.addBook("Atomic Habbit2")
l1.addBook("Atomic Habbit3")
l1.showInfo()