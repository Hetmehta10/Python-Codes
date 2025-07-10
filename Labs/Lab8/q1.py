# Add few names, one name in each row, in “name.txt file”.
# a. Count no of names
# b. Count all names starting with vowel
# c. Find longest name
def file():
        f = open("name.txt", 'r')
        # no of names
        a = f.read().split("\n")
        print("Number of names: ", len(a))
        # no of names starting with a vowel
        count = 0
        for i in a:
                if i[0].lower() in 'aeiou':
                        count += 1
        print("Number of names starting with a vowel: ", count)
        #Longest name
        name = ''
        for i in a:
                if len(i) > len(name):
                        name = i
        print("Longest name: '", name, "', With length: ", len(name))


file()