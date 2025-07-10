# Input two values from user where the first line contains N, the number of test cases. The next N lines contain the
# space separated values of a and b. Perform integer division and print a/b. Handle exception in case of
# ZeroDivisionError or ValueError.
# Sample input
# 1 0
# 2 $
# 3 1
# Sample Output :
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$' 3

n = int(input("Enter N: "))
for i in range(n):
        try:
                a = list(map(int, input("Enter numbers: ").split()))
                print("Ans: ", a[0]/a[1])
        except ValueError :
                print("Error Code: invalid literal for int() with base 10: '$' 3")
        except  ZeroDivisionError:
                print("Error Code: integer division or modulo by zero")