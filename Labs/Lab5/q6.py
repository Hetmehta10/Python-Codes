# Program to count number of unique words in a given sentence using sets.
string = input("Enter string: ")
a = set(string.upper().split())
print("Count of unique words = ",len(a))