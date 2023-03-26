def selectionSort(x):
    n = len(x)
    for i in range(0, n):
        for j in range(i+1, n):
            if x[j] < x[i]:
                x[i], x[j] = x[j], x[i]
    return x