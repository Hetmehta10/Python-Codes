# Write functions to explain mentioned concepts:
# a) Keyword argument
# b) Default argument
# c) Variable length argument
# Keywords argument
def printab(a, b):
    print(a)
    print(b)


printab(b=200, a=100)


# Default argument
def printab(a=100, b=200):
    print(a)
    print(b)


printab()


# Variable length non keyword argument
def printab(*a):
    print(a)


printab(1, 2, 3, 4, 5, 6, 7, 8, 9)

# variable length keyword argument
def printab(**a):
    print(a)


ab = {'av':2, 'ab':4}
printab(**ab)