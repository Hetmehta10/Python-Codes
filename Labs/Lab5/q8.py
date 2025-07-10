# Take two sets and apply various set operations on them :
# S1 = {Red ,yellow, orange , blue }
# S2 = {violet, blue , purple}
s1 = {'Red', 'yellow', 'orange', 'blue'}
s2 = {'violet', 'blue', 'purple'}
print(s1.union(s2))  # union  of 2 sets
print(s1.intersection(s2))  # intersection of 2 sets
print(s1.symmetric_difference(s2))  # symmetric difference of 2 sets
s1.add('green')
print(s1)
s3 = s1.copy()
print(s3)
print(s1.difference(s2))  # s1 - s2
s1.discard('green')
print(s1)
print(s1.issubset(s2))
s1.remove('Red')
print(s1)