'''Write a program to compute the length of the hypotenuse (c) of a
right triangle using Pythagoras theorem. 
'''
from math import sqrt
a=float(input("Enter 1 side: "))
b=float(input("Enter 2nd side: "))
c=sqrt(a*2+b*2)
print(c)