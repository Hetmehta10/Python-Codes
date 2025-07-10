# Write a lambda function which gives tuple of max and min from a list.
# Sample input: [10, 6, 8, 90, 12, 56]
# Sample output: (90,6)
a = lambda lst: (max(lst), min(lst))
ls = list(map(int, input("Enter list: ").split()))
print(a(ls))