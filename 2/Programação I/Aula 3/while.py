valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor < 0:
        break
    valores.append(valor)
media = sum(valores)/(len(valores))
print(f'Valores digitados: {valores}\nMédia: {media}')