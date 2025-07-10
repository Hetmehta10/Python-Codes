# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers
# smaller than the specified number.
def sum_of_cubes(n):
    s = 0
    for i in range(n):
        s += i**3
    return s


n = int(input("Enter n: "))
print("Sum of cubes of smaller term: ", sum_of_cubes(n))
