def convTemp(t,e):
    if (e == 'c') or (e == 'C'):
        res = (((t - 32) * 5)/9)
        print(f"A temperatura digitada {t} equivale a {res} na escala {e}")
    elif (e == 'f') or (e == 'F'):
        res = ((t * 9)/5) + 32
        print(f"A temperatura digitada {t} equivale a {res} na escala {e}")
    else:
        print("O valor digitado de escala é inválido, programa finalizado.")

temp = float(input("Digite a temperatura: "))
escala = input("Qual escala deseja converter? ‘c’ – Celsius / ‘f’ – fahrenheit ")
convTemp(temp,escala)