def imc(p, a):
    res = round((p / (a * a)),2)
    if res < 18.5:
        print(f"Seu IMC é {res}, classificação: Peso Baixo")
    elif (res >= 18.5) and (res <= 24.9):
        print(f"Seu IMC é {res}, classificação: Peso Normal")
    elif (res >= 25.0) and (res <= 29.9):
        print(f"Seu IMC é {res}, classificação: Sobrepeso")
    elif (res >= 30.0) and (res <= 34.9):
        print(f"Seu IMC é {res}, classificação: Obesidade (Grau I)")
    elif (res >= 35.0) and (res <= 39.9):
        print(f"Seu IMC é {res}, classificação: Obesidade Severa (Grau II)")
    else:
        print(f"Seu IMC é {res}, classificação: Obesidade Mórbida (Grau III)")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))    
imc(peso, altura)