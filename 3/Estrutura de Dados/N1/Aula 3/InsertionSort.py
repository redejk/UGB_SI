def insertionSort(x):
    n = len(x)
    for i in range(1, n):
        atual = x[i]
        j = i - 1
        while j >= 0 and atual < x[j]:
            x[j+1] = x[j]
            j = j - 1
        x[j+1] = atual
    return x