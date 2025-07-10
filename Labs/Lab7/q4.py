# Write a recursive function to print Fibonacci series upto n terms.
def fibonacci(t, a=0, b=1):
    if t == 0:
        return
    print(a)
    fibonacci(t-1, b, a+b)


n = int(input("Enter n: "))
fibonacci(n)