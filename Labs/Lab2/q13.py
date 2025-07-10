'''Using membership operator find whether a given character is in a string.'''
a=input("Enter a string: ")
b=input("Enter character: ")
if b in a:
        print("Yes",b,'in the string',a)
else:
        print("No",b,'not in string',a)