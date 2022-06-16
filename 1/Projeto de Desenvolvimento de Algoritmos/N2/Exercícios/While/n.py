n = 0
soma = 0
cont = 0
while n >= 0:
    n = float(input("Digite um valor: "))
    soma = soma + n
    cont = cont + 1
media = (soma / cont)
print(f"Total de valores lidos: {cont} \nSoma dos valores lidos: {soma} \nMédia dos valores lidos: {media}")
