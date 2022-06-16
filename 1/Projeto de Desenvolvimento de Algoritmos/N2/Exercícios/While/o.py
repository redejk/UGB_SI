cont = 1
fatorial = 1
while (cont <= 10):
    if (cont % 2) != 0:
        n = cont
        while (n > 1):
            fatorial = fatorial * n
            n = n -1
        print(f"O fatorial de {cont} é : {fatorial}")
        fatorial = 1    
    cont = cont + 1