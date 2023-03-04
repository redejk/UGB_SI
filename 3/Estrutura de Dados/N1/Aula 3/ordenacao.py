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
        for i in range(0, n):
            for j in range(i+1, n):
                if x[j] < x[i]:
                    x[i], x[j] = x[j], x[i]
        return x

    def insertionSort(self, x):
        n = len(x)
        for i in range(1, n):
            atual = x[i]
            j = i - 1
            while j >= 0 and atual < x[j]:
                x[j+1] = x[j]
                j = j - 1
            x[j+1] = atual
        return x
    
    def shellSort(self, x):
        h = 1
        n = len(x)
        while h < n:
            h = h * 3 + 1
        while h > 1:
            h = h // 3
            for i in range(h, n , h):
                atual = x[i]
                j = i - h
                while j >= 0 and atual < x[j]:
                    x[j+h] = x[j]
                    j = j - h
                x[j+h] = atual
        return x
    
ordenacao = Ordenacao()

y = [6,4,7,3,5]

# print(ordenacao.bubbleSort(y))
# print(ordenacao.selectionSort(y))
# print(ordenacao.insertionSort(y))
# print(ordenacao.shellSort(y))