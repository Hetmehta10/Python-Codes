# Create numpy array to find sum of all elements in an array.
import numpy as np
a = []
n = int(input("Enter n: "))
for i in range(n):
        a.append(int(input("Enter number: ")))

b = np.array(a)
print("Sum of array: ", np.sum(b))