def bubbleSort(x):
    n = len(x)
    for i in range(0, n-1):
        for j in range(n-1, 0, -1):
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1], x[j]
    return x