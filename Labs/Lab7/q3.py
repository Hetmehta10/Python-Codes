#  Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
def one_to_n(n):
    if n == 1:
        print(n)
    else:
        one_to_n(n-1)
        print(n)


n = int(input("Enter number: "))
one_to_n(n)