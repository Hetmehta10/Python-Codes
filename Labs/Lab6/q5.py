# Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name, year,
# director name, production cost, collection made (earning) & perform the following :-
# a) print all movie details
# b) display name of movies released before 2015
# c) print movies that made a profit.
# d) print movies directed by a particular director.

n = int(input("Enter the number of movies: "))
movies = []

for i in range(n):
    print(f"Enter details for movie {i + 1}:")
    name = input("Name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    production_cost = float(input("Production Cost: "))
    collection = float(input("Collection Made: "))

    movie = {
        'name': name,
        'year': year,
        'director': director,
        'production_cost': production_cost,
        'collection': collection
    }

    movies.append(movie)

print("\nMovie Details:")
print("-----------------------------------")
for movie in movies:
    print("Name:", movie['name'])
    print("Year:", movie['year'])
    print("Director:", movie['director'])
    print("Production Cost:", movie['production_cost'])
    print("Collection Made:", movie['collection'])
    print("-----------------------------------")

print("Movies released before 2015:")
for movie in movies:
    if movie['year'] < 2015:
        print(movie['name'])

print("\nProfitable Movies:")
for movie in movies:
    if movie['collection'] > movie['production_cost']:
        print(movie['name'])

director_name = input("\nEnter director's name to search for movies directed by them: ")
print(f"Movies directed by {director_name}:")
for movie in movies:
    if movie['director'] == director_name:
        print(movie['name'])