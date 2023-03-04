def selectionSort (x):
  n = len(x)
  print(x)
  for i in range(0, n-1):
    atual = i
    for j in range(i+1, n):
      if x[j] < x[atual]:
        atual = j
    x[i], x[atual]  = x[atual], x[i]
    print(i, 'vetor: ', x)
  return x

y = [1,2,4,7,8,3]
print(selectionSort(y))
