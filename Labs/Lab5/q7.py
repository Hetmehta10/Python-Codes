# Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
# a) Fruits which are in both sets s1 and s2
# b) Fruits only in s1 but not in s2
# c) Count of all fruits from s1 and s2
s1 = set(input("Enter the set: ").lower().split())
s2 = set(input("Enter the set: ").lower().split())
print("Fruits common in both : ", s1.intersection(s2))
print("Fruits only in s1 but not s2: ", s1.symmetric_difference(s2))
print("Count of all fruits in s1 and s2: ", len(s1.union(s2)))