cont = 0
proximo = 0
while (cont >= 0) and (cont <= 14):
    if (cont == 0):
        atual = 0
        print(atual)
        cont = cont + 1
    elif (cont == 1):
        anterior = 0
        atual = 1
        print(atual)
        cont = cont + 1
    while (cont >= 2) and (cont <= 14):
        proximo = atual + anterior
        print(proximo)
        anterior = atual
        atual = proximo
        cont = cont + 1
        