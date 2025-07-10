# Store integers in a file.
# a. Find the max number
# b. Find average of all numbers
# c. Count number of numbers greater than 100
def file():
        f = open("integer.txt", 'r')
        # max number
        a = f.read().split("\n")
        j = 0
        for i in a:
                a[j] = int(i)
                j += 1
        print("Max number: ", max(a))
        # Avweage
        count = 0
        s = 0
        for i in a:
                s += i
                count += 1
        print("Average: ", count/s)
        #Number greater than 100
        print("Number greater than 100: ")
        for i in a:
                if i > 100:
                        print(i)
        


file()