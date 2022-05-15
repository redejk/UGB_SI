base = int(input("Digite um valor para base que seja positivo: "))
expoente = int(input("Digite um valor para o expoente que seja positivo: "))
cont= 1
resultado = 1
while cont <= expoente:
    resultado = resultado * base
    cont = cont + 1
print(resultado)