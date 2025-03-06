#program to compute area and perimeter of a rectangle
class Rectangle:
    def  __init__(self,Length,Width):
        self.length=Length
        self.width= Width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
rect = Rectangle (6,3)
print (f"Area:{rect.area()}")
print (f"perimeter:{rect.perimeter()}")






        
        