def bubbleSort (x):
  n = len(x)
  print(x)
  for i in range(0, n-1):
    ordenado = True
    for j in range(n-1, i, -1):
      if x[j] < x[j-1]:
        x[j], x[j-1] = x[j-1], x[j]
        ordenado = False
    print(i, 'vetor: ', x)
    if ordenado:
      break
  return x

y = [1,2,4,7,8,3]
print(bubbleSort(y))