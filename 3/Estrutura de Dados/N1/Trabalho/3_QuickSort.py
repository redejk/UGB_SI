import time
import random

def quicksort(vet, inicio=0, fim=None):
    fim = fim if fim != None else len(vet)-1
    if inicio < fim:
        pivo = particao(vet, inicio, fim)
        quicksort(vet, inicio, pivo-1)
        quicksort(vet, pivo+1, fim)

def particao(vet, inicio, fim):
    pivo = vet[fim]
    i = inicio
    for j in range(inicio, fim):
        if vet[j] <= pivo:
            vet[i], vet[j] = vet[j], vet[i]
            i += 1
    vet[i], vet[fim] = vet[fim], vet[i]
    return i

#a)Ordenado 5000
vet = []
for i in range(1,5001):
    vet.append(i)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)
print(len(vet))

# #a)Ordenado 10000
vet = []
for i in range(1, 10001):
  vet.append(i)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

# #b)Ordem inversa 5000
vet = []
for i in range(5000, 0, -1):
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
vet = random.sample(range(1, 15000), 5000)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#c)Ordem aleatoria 1 10000
vet = []
vet = random.sample(range(1, 15000), 10000)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#d)Ordem aleatoria 2 5000
vet = []
vet = random.sample(range(3000, 15000), 5000)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#d)Ordem aleatoria 2 10000
vet = []
vet = random.sample(range(3000, 15000), 10000)
inicio = time.time()
quicksort(vet)
fim = time.time()
print(vet)
print(fim - inicio)