def powerset(string):
    x = len(string)
    for i in range(0, 2 ** x):
        subset = []
        for j in range(0, x):
            if (i >> j) & 1==1:
                subset.append(string[j])
        print(''.join(subset))



powerset("abc")
