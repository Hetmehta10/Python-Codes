# Write a program to count and display the number of capital letters in a given string.

string = input("Enter the string: ")
count = 0
for i in string:
    if i.isupper():
        count += 1
print("The number of upper case letter in the string is ", count)