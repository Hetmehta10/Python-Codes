# Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.
a=int(input("Enter number: "))
b=int(input("Enter number: "))
if a>b:
        print(a,'is greater than',b)
elif a==b:
        print('numbers are equal')
else:
        print(b,'is greater than',a)