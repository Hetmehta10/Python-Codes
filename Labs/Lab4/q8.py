# Convert all lower cases to upper case in a string.

a = input("Enter a string: ")
for i in a:
    if i.islower():
        a = a.replace(i, i.upper())
print(a)