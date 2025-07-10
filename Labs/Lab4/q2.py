# Find whether the given number is Armstrong number.

num = int(input("Enter number: "))
a = num
b = 0
n = 0
while a > 0:
    n = n + 1
    a = a//10
a = num
while a > 0:
    b = b + (a % 10)**n
    a = a//10

if num == b:
    print("The number", num, "is an armstrong number")
else:
    print("THe number", num, "is not an armstrong number")