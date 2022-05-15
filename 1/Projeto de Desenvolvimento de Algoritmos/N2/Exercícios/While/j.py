celsius = 0
fahrenheit = 0
cont = 10
while (cont >= 10) and (cont <= 100):
    celsius = cont
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} ºC = {fahrenheit} ºF")
    cont = cont + 10