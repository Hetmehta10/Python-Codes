# Write a lambda function to find volume of cone.
from math import pi
a = lambda x, y: (pi*x*x*y)*1/3
rad = int(input("Enter radius: "))
height = int(input("Enter height: "))
print("Volume of Cone: ", a(rad, height))