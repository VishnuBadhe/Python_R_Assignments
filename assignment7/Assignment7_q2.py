# 1. Define a Book class with the following attributes: Title, Author (Full name), Price.
#    A:- Define a constructor used to initialize the attributes of the method with values entered by the user.
#    B:-The View() method to display information for the current book.
#    C:-Write a program to testing the Book class.

class Book:
    def __init__(self):
        self.title = input(f"Enter title of the book: ")
        self.author = input(f"Enter Author's full name: ")
        self.price = input(f"Enter price of the book: ")

    def view(self):
        print(f"---Information of the current book---")
        print(f"title = {self.title}")
        print(f"author = {self.author}")
        print(f"price = {self.price}")

b = Book()
print(b.__dict__)
b.view()




