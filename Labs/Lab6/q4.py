# Create a dictionary of n persons where key is name and value is city.
# a) Display all names
# b) Display all city names
# c) Display student name and city of all students.
# d) Count number of students in each city
n = int(input("Enter n: "))
dic = {}
for i in range(n):
    name = input("Enter name:")
    dic[name] = input("Enter city: ")
# 1)
print("Names: ")
for i in dic:
    print(i)  # for name
print("------------------------------------")
# 2)
print("City: ")
city = [i for i in dic.values()]
city = set(city)
for i in city:
    print(i)
print("------------------------------------")
# 3)
print("Name and City: ")
for i in dic:
    print("Name: %s, City: %s" % (i, dic[i]))
print("------------------------------------")
# 4)for city and its count
print("City and Count:")
dic2 = {}
for i in city:
    dic2[i] = 0
for i in dic:
    if dic[i] in dic2.keys():
        dic2[dic[i]] += 1
print(dic2)