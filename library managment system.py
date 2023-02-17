#  borrow =, return book details
class library:
    def __init__(self,listofbookss):
        self.books = listofbookss

    def displayAvaliblebooks(self):
        print("books are present in this library are: ")
        for book in self.books:
            # print(book)
            print('*' +book)
    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. please keep it safe and retun it with in 30 days ")
            self.books.remove(bookname)
            return True 
        else:
            print("sorry ,this book is either not avalible or has already issued to someone else, please wait until the book is return")
            return False

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("thanks for returning this book, have a great day")
        


class student:
    def requestbook(self):
        self.book = input("Enter the book which you want to borrow : ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the book which you want to return : ")
        return self.book

if __name__ == "__main__":
    centraLibrary = library(["Algorith","Rd sharma","django","pyton"])
    student = student()
    # centraLibrary.displayAvaliblebooks()

    while(True):
        welcomeMsg = '''********WElcome to central library******** 
        please choose an options:
        1. List all the books.
        2. Request a book .
        3. Add or Return a book .
        4. Exit the library.
        '''
        print(welcomeMsg)
    
        a = int(input("Enter a choice :"))
        if a == 1 :
         centraLibrary.displayAvaliblebooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestbook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("thanks for visiting here , have a great day")
            exit()
        else:
            print("invalid choose")

       
