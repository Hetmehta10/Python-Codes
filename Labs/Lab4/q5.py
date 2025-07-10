# Check whether given number is palindrome or not.

num = int(input("Enter a number: "))
a = num
b = 0
while a > 0:
    b = b*10 + (a % 10)
    a = a//10
if b == num:
    print("The number", num, "is a palindrome")
else:
    print("The number", num, "is not a palindrome")