class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

while True:
    radius = float(input("Enter the radius of your circle : "))
    if radius > 0:
        break
    print("Invalid input! Radius must be greater than zero.")

circ = Circle(radius)

print(f"Area: {circ.area()}")
print(f"Circumference: {circ.circumference()}")
