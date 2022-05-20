cont = 1
dobrar = 0
while (cont >= 1) and (cont <= 64):
    if (cont == 1):
        graos = 1
        cont = cont + 1
    else:
        while (cont >= 2) and (cont <= 64):
            dobrar = ((cont - 1)* 2)
            graos = (dobrar + graos)
            cont = cont + 1
print(graos)
