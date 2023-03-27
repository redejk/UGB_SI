import time
import random

def quicksort(vet, inicio=0, fim=None):
    fim = fim if fim != None else len(vet)-1
    if inicio < fim:
        pivo = insertionSort(vet, inicio, fim)
        quicksort(vet, inicio, pivo-1)
        quicksort(vet, pivo+1, fim)

def insertionSort(vet, inicio, fim):
    for i in range(inicio+1, fim+1):
        atual = vet[i]
        j = i - 1
        while j >= 0 and atual < vet[j]:
            vet[j+1] = vet[j]
            j = j - 1
        vet[j+1] = atual
    return j + 1

#a)Ordenado 5000
vet = []
for i in range(1,988):
    vet.append(i)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)
print(len(vet))

# #a)Ordenado 10000
vet = []
for i in range(1, 988):
  vet.append(i)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

# #b)Ordem inversa 5000
vet = []
for i in range(987, 0, -1):
  vet.append(i)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

# #b)Ordem inversa 10000
vet = []
for i in range(10000, 0, -1):
  vet.append(i)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#c)Ordem aleatoria 1 5000
vet = []
vet = random.sample(range(1, 15000), 988)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

# #c)Ordem aleatoria 1 10000
vet = []
vet = random.sample(range(1, 15000), 988)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

# #d)Ordem aleatoria 2 5000
vet = []
vet = random.sample(range(3000, 15000), 988)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

# #d)Ordem aleatoria 2 10000
vet = []
vet = random.sample(range(3000, 15000), 988)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)