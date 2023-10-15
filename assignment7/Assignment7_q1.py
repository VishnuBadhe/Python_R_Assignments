 # Que1
 # Circle class
 # 1 - Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the
 #     constructor:
 #     def init (self,a,b,r):
 #     self.a = a
 #     self.b = b
 #     self.r = r
 #     A:- Define a Area() method of the class which calculates the area of the circle.
 #     B:-Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


class Circle:
    def __init__(self, area=0, perimeter=0):
        self.radius = int(input(f"Enter a radius: "))
        self.area = area
        self.perimeter = perimeter


    def area1(self):
        self.area = self.radius ** 2 * 3.14
        print(f"Area of Circle:",{self.area})


    def perimeter1(self):
        self.perimeter = 2 * 3.14 * self.radius
        print(f"Perimeter of Circle:",{self.perimeter})


c = Circle()
c.area1()
c.perimeter1()





