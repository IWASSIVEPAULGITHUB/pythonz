# program to calculate the volume of a sphere given the radius

#Ask for radius input and calculate the volume
import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3 )* math.pi * math.pow(radius,3)

print(f"the volume o fthe sphere is {volume:.2f}")
