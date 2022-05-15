expoente = 0
base = 3
resultado = 0
while (expoente >= 0) and (expoente <= 15):
    if (expoente == 0):
        resultado = 1
        print(resultado)
    elif (expoente == 1):
        resultado = base
        print(resultado)
    else:
        resultado = resultado * base
        print(resultado)
    expoente = expoente + 1
