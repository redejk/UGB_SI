cont = 1
soma = 0
media = 0
while (cont <= 10):
    n = float(input("Digite um valor: "))
    soma = soma + n
    cont = cont + 1
media = (soma / (cont -1))
print(f"A soma dos valores digitados é: {soma} e a média entre eles é: {media}")