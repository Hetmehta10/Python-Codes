# Scan n values in range 0-3 and print the number of times each value has occurred.
value = {0: 0, 1: 0, 2: 0, 3: 0}
scan = []
n = int(input('Enter n: '))
for i in range(n):
    scan.append(int(input("Enter the number: ")))
for i in scan:
    if i in value.keys():
        value[i] += 1

for i in value:
    print("The count of %d = %d" % (i, value[i]))