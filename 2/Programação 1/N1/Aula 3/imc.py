peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso / (altura**2))
print(imc)
if imc <= 18.5:
    print('Abaixo do peso')
elif (imc >= 18.6) and (imc <= 24.9):
    print('Peso ideal (Parabéns!)')
elif (imc >= 25) and (imc <= 29.9):
    print('Levemente acima do peso')
elif (imc >= 30) and (imc <= 34.9):
    print('Obesidade Grau 1')
elif (imc >= 35) and (imc <= 39.9):
    print('Obesidade Grau 2 (Severa)')
else:
    print('Obesidade 3 (Mórbida)')
