cont = 50
soma = 0
while (cont >= 50) and (cont <= 70):
    if (cont % 2) == 0:
        soma = (soma + cont)
    cont = cont + 1
media = (soma / (cont -1))
print(f"A soma dos valores pares entre 50 e 70 é: {soma} e a média aritmética entre eles é: {media}")