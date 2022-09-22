valores = []
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break
    else:
        valores.append(valor) #Criei a lista valores com cada valor digitado diferente de -1
media = f'{sum(valores)/(len(valores)):.2f}' #calculei a media, somando os valores dividindo pela quantidade (somente 2 casas decimais)
valores_nao_repetidos = set() #crio um conjunto
valores_nao_repetidos.update(valores) #coloco dentro do conjunto os valores da lista, por ser um conjunto, só irá ficar os valores únicos
dicionario_valores = {} #crio um dicionário
for i in valores_nao_repetidos: #para cada valor que existe no conjunto
    dicionario_valores.update({i:0})  #eu crio {i:0} (ou seja para cada i estou criando uma chave com valor inicial 0)
for j in valores: #para cada valor na lista valores
    if j in dicionario_valores.keys(): #comparo se o j existe como chave no dicionário
        dicionario_valores[j] +=1 #Caso existir, eu pego o valor da chave [j] e acrescento +1
key_maior_valor = max(dicionario_valores, key=dicionario_valores.get)
"""Explicando a linha acima. Estou pegando o maior value e gravando a key variável key_maior_valor
Após a execução dos 'for' anteriores, fui somando +1 na value quando a key já existia no dicionário
"""
maior_valor = dicionario_valores[key_maior_valor]
chaves_com_maior_valor = []
for x in dicionario_valores.keys():
    if dicionario_valores[x] == maior_valor:
        chaves_com_maior_valor.append(x)
"""Explicando as linhas acima. com a variável maior_valor estou pegando o valor referente a key_com_maior_valor encontrada anteriormente
Crio uma lista chaves_com_maior_valor e faço um x, para que cada chave dentro do dicionário, irá ser comparado se o valor dessa chave
é igual ao valor da variável maior_valor, se for irá ser adicionado na lista chaves_com_maior_valor
"""
print(f'Lista completa de valores:\n{valores}\nValores que não se repetem:\n{valores_nao_repetidos}\nDicionário completo com a quantidade de cada valor:\n{dicionario_valores}\nA média é: {media}')

if len(valores) == len(valores_nao_repetidos):
    print('Não há moda')
elif len(chaves_com_maior_valor) == 1:
    print(f'A moda é unimodal: {chaves_com_maior_valor}')
elif len(chaves_com_maior_valor) == 2:
    print(f'A moda é bimodal: {chaves_com_maior_valor}')
elif len(chaves_com_maior_valor) >= 3:
    print(f'A moda é multimodal: {chaves_com_maior_valor}')
"""
Faço a comparação da quantidade de valores que existem dentro da variável chaves_com_maior_valor e retorno no print o tipo da moda, caso exista
"""