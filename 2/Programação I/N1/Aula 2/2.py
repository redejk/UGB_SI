print('Construir um algoritmo para calcular a média de um conjunto de valores inteiros e positivos.')
conjunto = []
while True:
    valor = int(input('Digite um valor: '))
    if valor <= 0:
        print('Digite um valor inteiro e positivo')
        continue
    else:
        conjunto.append(valor)
        while True:
            resposta = input('Deseja digitar outro valor? S/N ')
            if resposta == 's' or resposta == 'S':
                valor = int(input('Digite um valor: '))
                if valor <= 0:
                    print('Digite um valor inteiro e positivo')
                else:
                    conjunto.append(valor)
            elif resposta == 'n' or resposta == 'N':
                break
            else:
                print('Resposta inválida')
                continue
        break
soma = 0
for v in conjunto:
    soma = soma + v

media = soma / (len(conjunto))

print(f'Valores dentro do conjunto: {conjunto}\nSoma dos valores: {soma}\nQuantidade de valores: {len(conjunto)}\nA média entre os valores do conjunto é: {media}')
