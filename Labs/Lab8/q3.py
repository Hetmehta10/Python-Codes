# Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ):
# Example:
# Dehradun 5.78 308.20
# Delhi 190 1484
# ……………
# Open file city.txt and read to:
# a. Display details of all cities
# b. Display city names with population more than 10Lakhs
# c. Display sum of areas of all cities
def file():
        f = open("city.txt", 'r')
        a = f.read().split("\n")
        city = []
        for i in a:
                city.append(i.split())
        # Display details of city
        for i in city:
                for j in i:
                        print(j, end='  ')
                print()
        # cities with population more than 10l
        print("cities with population more than 10l: ")
        for i in city:
                j = i[1]
                if float(j) > 10 :
                        print(i[0])
        # sum of areas
        s = 0
        for i in city:
                j = i[2]
                s += float(j)
        print("sum of areas: ", s)

        
file()