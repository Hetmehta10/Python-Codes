# Write a Python function to find the maximum and minimum numbers from a sequence of numbers. (Note: Do not
# use built-in functions.)

def max_and_min(seq):
    maxterm = seq[0]
    minterm = seq[0]
    for i in range(len(seq)):
        if maxterm < seq[i]:
            maxterm = seq[i]

        if minterm > seq[i]:
            minterm = seq[i]

    print("Max Term: ", maxterm)
    print("Min Term: ", minterm)


a = [12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_and_min(a)