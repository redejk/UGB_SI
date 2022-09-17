valores = []
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break
    else:
        valores.append(valor)
media = sum(valores)/(len(valores))
repetidos = set()
for i in valores:
    repetidos.add(i)
for i in range(len(repetidos)):
    print(i)
    print('\n')
#print(f'A moda dos valores digitados é: {moda}\ne a média é: {media}')