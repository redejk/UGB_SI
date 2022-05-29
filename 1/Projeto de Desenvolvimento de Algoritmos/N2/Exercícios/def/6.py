def fahrenheit(t):
    res = ((t * 9)/5) + 32
    return res 

temp = float(input("Digite a temperatura em graus celsius: "))
f = fahrenheit(temp)
print(f"A temperatura digitada: {temp}º equivale a {f}ºF")