import statistics
valores = []
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break
    else:
        valores.append(valor) #Criei a lista valores com cada valor digitado diferente de -1
media = f'{sum(valores)/(len(valores)):.2f}' #calculei a media, somando os valores dividindo pela quantidade (somente 2 casas decimais)
moda = statistics.mode(valores)
print(f'Moda: {moda}\nMédia: {media}')