# Print all prime numbers between 1 and 100.
for i in range(2, 101):
    counter = 0
    for j in range(2, i):
        if i % j == 0:
            counter += 1
            break
    if counter == 0:
        print(i)