# Find the greatest among three numbers assuming no two values are same.
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
n3=int(input("Enter 3rd number: "))
if n1>n2 and n1>n3:
        print('biggest number',n1)
elif n2>n3:
        print('biggest number',n2)
else:
        print('biggest number',n3)