 # 1. Create two classes:
 #    A:- Author: authorName ,age,place
 #    B:- Book: name ,price
 #    C:- relationship: Book has-an Author
 #    D:-add print method in Both class



class Author:
    def __init__(self, authorName, age, place):
         self.authorName = authorName
         self.age = age
         self.place = place



    def print_details(self):
        print(f"------Author Details------")
        print(f"authorName = {self.authorName}")
        print(f"age = {self.age}")
        print(f"place = {self.place}")



class Book:

    def __init__(self, name, price, authorName, age, place):
        self.name = name
        self.price = price
        self.author = Author(authorName, age, place)

    def print_details(self):
        print(f"------Book Details------")
        print(f"name = {self.name}")
        print(f"price = {self.price}")
        self.author.print_details()


b = Book('Wings of Fire', 650, 'A.P.J. Abdul kalam', 70, 'chennai')
print(b.__dict__)
b.print_details()






































# class Book:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#         def print_book_details(self):
#             print(f"name = {self.name}")
#             print(f"price = {self.price}")
#             print(f"-----Author details-----")
#             self.author.print_details()
#
#
#
# class Author:
#
#     def __init__(self, authorName, age, place,name):
#         self.authorName = authorName
#         self.age = age
#         self.place = place
#         self.book=Book(name,price)
#
#         def print_details(self):
#             print(f"authorName = {authorName}")
#             print(f"age = {self.age}")
#             print(f"place = {self.place}")
#
# # b1 = Book('Wings of Fire', 350, 'A.P.J. Abdul Kalam', 70, 'chennai')
# A1= Author()
# print(b1.__dict__)
# b1.print_book_details()
#
#
#
