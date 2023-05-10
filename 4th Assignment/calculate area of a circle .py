# 4. Write a python script which takes the radius from the user and display area of a circle.


import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is {area:.2f}")
