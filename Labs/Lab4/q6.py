# Write a program to print sum of digits.
num = int(input("Enter the number: "))
a = num
sumnum = 0
while a > 0:
    sumnum += a % 10
    a = a//10
print("The sum of digits of number", num, "is", sumnum)