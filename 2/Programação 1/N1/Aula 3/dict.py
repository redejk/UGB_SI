from re import A


a = {'nome': 'carlos'}
#pega o valor pela chave
print(a['nome'])
#caso a chave for número, passar o número=chave
a = {0: 'carlos'}
print(a[0])
#atribuir um valor para a chave determinada, substituindo o valor que estava anteriormente
a[0] = 'ugb'
print(a[0])
#deletar o valor da chave
#del(a[0])
#limpa o dicionário
#a.clear()
#igualar um dicionário
#b = a
#b[0] = 'carro'
#print(b, a)
#criar uma copia de um dicionário
#b = a.copy()
b = a
b[0] = 'carro'
a[0] = 'jetta'
print(b, a)
print(b.items(), b.keys(), b.values())
