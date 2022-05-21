numero = int(input("Digite um número: "))
if (numero <= 0):
    print("Valor digitado é negativo, programa finalizado!")
    maior = menor = numero
else:
    maior = menor = numero
    while (numero >=0):
        numero = int(input("Digite um valor: "))
        if (numero > maior):
            maior = numero
        if (numero < menor) and (numero >= 0):
            menor = numero
    print(f"O maior valor digitado é: {maior} e o menor valor é : {menor}")
