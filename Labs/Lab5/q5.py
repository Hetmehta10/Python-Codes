# Given a string containing both upper and lower case alphabets. Write a Python program to count the number of
# occurrences of each alphabet (case insensitive) and display the same.
# Sample Input
# ABaBCbGc
# Sample Output
# 2A
# 3B
# 2C
# 1G
string = input("Enter string: ")
b = ""
for i in string.upper():
    if i not in b:
        print("%d'%s'" % (string.upper().count(i), i))
        b = b + i