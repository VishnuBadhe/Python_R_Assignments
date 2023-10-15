# Que2
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width
# attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to
# calculate the area of the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created
# using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with a height attribute and
# another Volume() method to calculate the volume of the Parallelepiped

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * self.length * self.width


    def area(self):
        return self.length * self.width


    def display_rectangle(self):
        print(f"---Parameters and Methods---")
        print(f"length = {self.length}")
        print(f"width = {self.width}")
        print(f"Perimeter of Rectangle = {self.perimeter()}")
        print(f"Area of Rectangle = {self.area()}")



class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def display_para(self):
        Rectangle.display_rectangle(self)
        print(f"height = {self.height}")
        print(f"Volume of Parallelepiped = {self.volume()}")


r = Rectangle(50, 40)
r.display_rectangle()

print()

p = Parallelepiped(50, 40, 35)
p.display_para()
# print(f"p = {p.__dict__}")












