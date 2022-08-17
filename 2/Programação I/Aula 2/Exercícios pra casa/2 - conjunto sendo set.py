print('Construir um algoritmo para calcular a média de um conjunto de valores inteiros e positivos.\nEvite digitar valores iguais, pois conjunto não permite valores duplicados.')
conjunto = set()
while True:
    valor = int(input('Digite um valor: '))
    if valor <= 0:
        print('Digite um valor inteiro e positivo')
        continue
    else:
        conjunto.add(valor)
        while True:
            resposta = input('Deseja digitar outro valor? S/N ')
            if resposta == 's' or resposta == 'S':
                valor = int(input('Digite um valor: '))
                if valor <= 0:
                    print('Digite um valor inteiro e positivo')
                elif valor in conjunto:
                    print(f'O valor {valor} já existe no conjunto, digite um valor diferente.')
                else:
                    conjunto.add(valor)
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

print(f'Valores dentro do conjunto: {conjunto}\nSoma dos valores: {soma}\nQuantidade de valores: {len(conjunto)}\nA média entre os valores digitados não duplicados foi: {media}')
