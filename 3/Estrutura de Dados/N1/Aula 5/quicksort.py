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
    print(i)
    return i

x = [3,2,8,10,1,5,9,4]
quicksort(x)
print(x)


