lst = [8]
lst[0] = 3
#Adiciona valores
lst.extend([1,2,3])
#Printa o valor na posição determinada
print(lst.index(3))
#Insere o valor, na posição determina
lst.insert(1,5)
#Remove o ultimo valor
lst.pop()
#Remove o valor determinado
lst.remove(1)
#Inverte a ordem
lst.reverse()
#organiza valor do menor para o maior
lst.sort()

print(lst)
