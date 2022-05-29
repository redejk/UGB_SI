def ObterFatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n-1
    return fatorial

numero = int(input("Digite um número: "))
print(ObterFatorial(numero))