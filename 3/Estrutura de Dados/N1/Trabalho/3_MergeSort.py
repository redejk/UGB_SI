import time
import random

def intercala(vet, inicio, meio, fim):
  x = vet[inicio:meio]
  y = vet[meio:fim]
  indX = 0
  indY = 0 
  i = inicio
  while i < fim:
    if x[indX] < y[indY]:
      vet[i] = x[indX]                     
      indX = indX + 1  

    else:
      vet[i] = y[indY]                 
      indY = indY + 1   
    i = i + 1 

    if indX == len(x):  
      vet[i: fim] = y[indY:len(y)] 
      break

    if indY == len(y): 
      vet[i:fim] = x[indX:len(x)] 
      break

def merge(vet, inicio, fim):
  if fim - inicio > 1:
    meio = (inicio + fim) // 2
    merge(vet, inicio, meio)
    merge(vet, meio, fim)
    intercala(vet, inicio, meio, fim)

def mergeSort(vet):
  merge(vet, 0, len(vet))

#MargeSort
#a)Ordenado 5000
vet = []
for i in range(1,5001):
  vet.append(i)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#a)Ordenado 10000
vet = []
for i in range(1, 10001):
  vet.append(i)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#b)Ordem inversa 5000
vet = []
for i in range(5000, 0, -1):
  vet.append(i)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#b)Ordem inversa 10000
vet = []
for i in range(10000, 0, -1):
  vet.append(i)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#c)Ordem aleatoria 1 5000
vet = []
vet = random.sample(range(1, 15000), 5000)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#c)Ordem aleatoria 1 10000
vet = []
vet = random.sample(range(1, 15000), 10000)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#d)Ordem aleatoria 2 5000
vet = []
vet = random.sample(range(3000, 15000), 5000)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)

#d)Ordem aleatoria 2 10000
vet = []
vet = random.sample(range(3000, 15000), 10000)
inicio = time.time()
mergeSort(vet)
fim = time.time()
print(vet)
print(fim - inicio)