class Ordenacao:
    def bubbleSort(self, x):
        n = len(x)
        qtd = 0
        for i in range(0, n-1):
            for j in range(n-1, 0, -1):
                if x[j] < x[j-1]:
                    qtd += 1
                    x[j], x[j-1] = x[j-1], x[j]
        return x, qtd

    def selectionSort(self, x):
        n = len(x)
        qtd = 0
        for i in range(0, n):
            for j in range(i+1, n):
                if x[j] < x[i]:
                    qtd += 1
                    x[i], x[j] = x[j], x[i]
        return x, qtd

    #def insertionSort(self, x):

crescente = []
for i in range(1, 1001):
    crescente.append(i)

decrescente = []
for i in range(1000, 0, -1):
    decrescente.append(i)

ordenacao = Ordenacao()

x, qtd_bubblesort_crescente = ordenacao.bubbleSort(crescente)

crescente = []
for i in range(1, 1001):
    crescente.append(i)

x, qtd_selectionsort_crescente = ordenacao.selectionSort(crescente)
#qtd_insertionsort_crescente = ordenacao.insertionSort(crescente)

x, qtd_bubblesort_decrescente = ordenacao.bubbleSort(decrescente)

decrescente = []
for i in range(1000, 0, -1):
    decrescente.append(i)

x, qtd_selectionsort_decrescente = ordenacao.selectionSort(decrescente)
# #qtd_insertionsort_decrescente = ordenacao.insertionSort(decrescente)

print(f"""Quantidade de execuções com vetor de 1000 posições ordenado em ordem crescente:
bubbleSort: {qtd_bubblesort_crescente}
selectionSort: {qtd_selectionsort_crescente}

Quantidade de execuções com vetor de 1000 posições ordenado em ordem decrescente:
bubbleSort: {qtd_bubblesort_decrescente}
selectionSort: {qtd_selectionsort_decrescente} 
""")

