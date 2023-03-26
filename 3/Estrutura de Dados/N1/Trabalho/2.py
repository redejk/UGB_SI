def quicksort(vet, inicio=0, fim=None):
    fim = fim if fim != None else len(vet)-1
    if inicio < fim:
        pivo = insertionSort(vet, inicio, fim)
        quicksort(vet, inicio, pivo-1)
        quicksort(vet, pivo+1, fim)

def insertionSort(vet, inicio, fim):
    for i in range(inicio, fim):
        atual = vet[i]
        j = i - 1
        while j >= 0 and atual < vet[j]:
            vet[j+1] = vet[j]
            j = j - 1
        vet[j+1] = atual
    return j

x = [3,2,1,4,8,5,9,10]
quicksort(x)
print(x)

#vetor_original = [3,2,1,4,8,5,9,10]
# atual = 3,2,8,10,1,5,9
# j = -1,0,-1,1,2,3,2,1,0,-1,4,3,2,5,4
# vet = 3,2,8,10,1,5,9

