# WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given
# string. String traversal will take place from left to right, not from right to left.
# Sample Input
# ABCDCDC
# CDC
# Sample Output
# 2

string = input("Enter string: ")
substring = input("Enter substring: ")
count = 0
a = 0
while True:
    a = string.find(substring, a)
    if a != -1:
        count += 1
        a += 1
    else:
        break

print("Number of occurance", count)