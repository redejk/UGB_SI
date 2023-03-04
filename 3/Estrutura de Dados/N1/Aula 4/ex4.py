def bubbleSort (x):
  n = len(x)
  for i in range(0, n-1):
    for j in range(i, n-1):
      if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j]
  return x

y = [1,2,4,7,8,3]
print(bubbleSort(y))