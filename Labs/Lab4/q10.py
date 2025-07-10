# Print the table for a given number:
# 5 * 1 = 5
# 5 * 2 = 10………..
num = int(input("Enter number: "))
for i in range(1,11):
    print("%d * %d = %d" % (num, i, num*i))