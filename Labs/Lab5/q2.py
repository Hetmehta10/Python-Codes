# Count total number of vowels in a given string.
a = 'aeiou'
string = input("Enter the string: ")
count = 0
for i in string:
    if i.lower() in a:
        count += 1

print("The number of vowels in the string is ", count)