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

x = [3,2,8,10,1,5,9,4]

quicksort(x)
print(x)





