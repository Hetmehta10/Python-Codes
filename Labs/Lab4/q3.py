# Print Fibonacci series up to given term
n = int(input('enter range for fabonachi series: '))
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(n-2):
    num3 = num1 + num2
    print(num3)
    num1, num2 = num2, num3