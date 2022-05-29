def fahrenheit(t):
    res = ((t * 9)/5) + 32
    print(f"A temperatura digitada: {t} equivale a {res} ºF")

temp = float(input("Digite a temperatura em graus celsius: "))
fahrenheit(temp)