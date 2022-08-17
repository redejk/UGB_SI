while True:
    A = int(input('Digite o primeiro valor: '))
    if A <= 0:
        print('O valor deve ser um inteiro positivo')
        continue
    else:
        break

while True:
    B = int(input('Digite o segundo valor: '))
    if B <= 0:
        print('O valor deve ser um inteiro positivo')
        continue
    else:
        break

while True:
    C = int(input('Digite o terceiro valor: '))
    if C <+ 0:
        print('O valor deve ser um inteiro positivo')
        continue
    else:
        break

if (A==B) and (A==C) and (B==C):
    print('O triângulo é Equilátero')
elif (A==B) or (A==C) or (B==C):
    print('O triângulo é Isósceles')
else:
    print('O triângulo não é do tipo Equilátero nem Isósceles')
