# Perform Matrix multiplication of any 2 n*n matrices.

import numpy as np
a = []
n = int(input("Enter number of n: "))
print("Matrix 1: ")
for i in range(n):
    c = []
    for j in range(n):
           c.append(int(input("Enter number: ")))
    a.append(c)
        
b = np.array(a)
a = []
print("Matrix 2: ")
for i in range(n):
        c = []
        for j in range(n):
                c.append(int(input("Enter number: ")))
        a.append(c)
d = np.array(a)
print(f'{b} * {d} = {b*d}')