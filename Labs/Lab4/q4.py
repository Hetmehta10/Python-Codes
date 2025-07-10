# Write a program to find if given number is prime number or not.
num = int(input("Enter a number: "))
prime = 0
for i in range(1, num+1):
    if num % i == 0:
        prime = prime+1
if prime > 2:
    print("The number", num, "is not a prime number")
else:
    print("The number", num, "is a prime number")