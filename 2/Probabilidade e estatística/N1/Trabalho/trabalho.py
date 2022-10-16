valores = []
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break
    else:
        valores.append(valor) 
media = f'{sum(valores)/(len(valores)):.2f}'
valores_nao_repetidos = set()
valores_nao_repetidos.update(valores)
dicionario_valores = {}
for i in valores_nao_repetidos:
    dicionario_valores.update({i:0})
for j in valores:
    if j in dicionario_valores.keys():
        dicionario_valores[j] +=1
key_maior_valor = max(dicionario_valores, key=dicionario_valores.get)
maior_valor = dicionario_valores[key_maior_valor]
chaves_com_maior_valor = []
for x in dicionario_valores.keys():
    if dicionario_valores[x] == maior_valor:
        chaves_com_maior_valor.append(x)
print(f'Lista completa de valores:\n{valores}\nValores que não se repetem:\n{valores_nao_repetidos}\nDicionário completo com a quantidade de cada valor:\n{dicionario_valores}\nA média é: {media}')

if len(valores) == len(valores_nao_repetidos):
    print('Não há moda')
elif len(chaves_com_maior_valor) == 1:
    print(f'A moda é unimodal: {chaves_com_maior_valor}')
elif len(chaves_com_maior_valor) == 2:
    print(f'A moda é bimodal: {chaves_com_maior_valor}')
elif len(chaves_com_maior_valor) >= 3:
    print(f'A moda é multimodal: {chaves_com_maior_valor}')