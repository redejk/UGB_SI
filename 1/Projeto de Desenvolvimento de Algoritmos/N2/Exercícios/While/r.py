numero = 0
maior = 0
menor = 0
while (numero >=0):
    numero = int(input("Digite um valor: "))
    if (numero > maior):
        maior = numero
    if (numero < menor) and (numero >= 0):
        menor = numero
print(f"O maior valor digitado é: {maior} e o menor valor é : {menor}")

