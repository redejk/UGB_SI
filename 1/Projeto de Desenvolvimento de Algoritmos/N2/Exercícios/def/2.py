def ObterFatorial():
    fatorial = 1
    n = int(input("Digite um número: "))
    while n > 1:
        fatorial = fatorial * n
        n = n-1
    print(fatorial)

ObterFatorial()