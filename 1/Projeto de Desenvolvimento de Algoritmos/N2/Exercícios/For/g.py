base = 3
resultado = 0
for i in range(0, 16):
    if (i == 0):
        resultado = 1
        print(resultado)
    elif (i == 1):
        resultado = base
        print(resultado)
    else:
        resultado = resultado * base
        print(resultado)
