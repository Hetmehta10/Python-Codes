# Create a tuple to store n numeric values and find average of all values.
n = int(input("Enter n: "))
tup = ()
for i in range(n):
    a = int(input("Enter the number: "))
    tup = tup + (a, )
s = 0
for i in tup:
    s += i
print('Average of the tuple', tup, "is ", s/n)
'''or 
print(sum(tup)/n)'''