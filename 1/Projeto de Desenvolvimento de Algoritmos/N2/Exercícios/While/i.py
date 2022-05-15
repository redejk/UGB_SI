atual = 0
anterior = 0
proximo = 0
cont = 0
while cont <=15:
    proximo = atual + anterior
    print(proximo)
    atual = cont + anterior
    anterior = atual - cont
    cont = cont +1
    