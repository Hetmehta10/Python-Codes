# Count and print all numbers divisible by 5 or 7 between 1 to 100.
count = 0
for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        count += 1
        print(i, end="  ")
print("\nTotal number of numbers between 1 and 100 divisible by 5 or 7 is ", count)