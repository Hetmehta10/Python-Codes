'''Write a Program where the radius is taken as input to compute the area
of a circle.
'''
from math import pi #math module
r=float(input("Enter the radius: "))
area=pi*r**2
print("Area = ",round(area,2))