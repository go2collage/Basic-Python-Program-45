# Python Program

# calculate Area and Circumference of Circle
# Using inbuilt Math Module

# import math lib.
import math

def circle_Circumference(radius):
    return 2 * math.pi * radius

def circle_Area(radius):
    return math.pi * radius * radius

radius = float(input("Enter Radius of Circle: "))

print("Given Radius of Circle is: ", radius)

print("Circumference of Circle is: ", circle_Circumference(radius))

print("Arear of Circle is: ", circle_Area(radius))

# Thanks for Watching