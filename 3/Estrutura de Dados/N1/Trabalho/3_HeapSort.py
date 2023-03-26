import time
import random

def geraHeap(vet, i, n):
  indM = i
  indFE = i * 2 + 1
  indFD = i * 2 + 2
  if indFE < n and vet[indFE] > vet[indM]:
    indM = indFE
  if indFD < n and vet[indFD] > vet[indM]:
    indM = indFD
  if indM != i:
    vet[i], vet[indM] = vet[indM], vet[i]
    geraHeap(vet, indM, n)

def heapSort(vet):
  n = len(vet)
  for i in range(n // 2 - 1, -1, -1):
    geraHeap(vet, i, n)

  for i in range(n-1, 0, -1):
    vet[i], vet[0] = vet[0], vet[i]
    geraHeap(vet, 0, i)

#HeapSort
#a)Ordenado 5000
vet = []
for i in range(1,5001):
  vet.append(i)
inicio = time.time()
heapSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#a)Ordenado 10000
vet = []
for i in range(1,10001):
  vet.append(i)
inicio = time.time()
heapSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#b)Ordem inversa 10000
vet = []
for i in range(10000, 0, -1):
  vet.append(i)
inicio = time.time()
heapSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#c)Ordem aleatoria 1 5000
vet = []
vet = random.sample(range(1, 15000), 5000)
inicio = time.time()
heapSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#c)Ordem aleatoria 1 10000
vet = []
vet = random.sample(range(1, 15000), 10000)
inicio = time.time()
heapSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#d)Ordem aleatoria 2 5000
vet = []
vet = random.sample(range(3000, 15000), 5000)
inicio = time.time()
heapSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#d)Ordem aleatoria 2 10000
vet = []
vet = random.sample(range(3000, 15000), 10000)
inicio = time.time()
heapSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)