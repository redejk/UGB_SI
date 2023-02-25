class Ordenacao:
    def bubbleSort(self, x):
        n = len(x)
        for i in range(0, n-1):
            for j in range(n-1, 0, -1):
                if x[j] < x[j-1]:
                    x[j], x[j-1] = x[j-1], x[j]
        return x

    def selectionSort(self, x):
        n = len(x)
        qtd = 0
        for i in range(0, n):
            for j in range(i+1, n):
                if x[j] < x[i]:
                    qtd +=1
                    x[i], x[j] = x[j], x[i]
        return x, qtd

    #def insertionSort(self, x):

ordenacao = Ordenacao()

y = [6,4,7,3,5]

print(ordenacao.bubbleSort(y))
print(ordenacao.selectionSort(y))