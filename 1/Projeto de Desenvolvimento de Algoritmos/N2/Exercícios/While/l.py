cont = 1
soma = 0
fatorial = 1
while (cont >= 1) and (cont <= 2):
    n = int(input("Digite um valor: "))
    while (n > 1):
        fatorial = fatorial * n
        n = n-1
    soma = soma + fatorial
    cont = cont + 1
    fatorial = 1
print(soma)
