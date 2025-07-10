'''Using membership operator find whether a given number is in
sequence (10,20,56,78,89)
'''
a=(10,20,56,78,89)
b=int(input("Enter number: "))
if b in a:
        print("Yes",b,'is in the sequence')
else:
        print("No",b,'is not in the sequence')