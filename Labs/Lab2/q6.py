'''Write a program to find area of triangle when length of sides are given.
'''
from math import sqrt
a=float(input("Enter side: "))
b=float(input("Enter side: "))
c=float(input("Enter side: "))
s=(a+b+c)/2
area=sqrt(s*(s-a)(s-b)(s-c))
print(area)