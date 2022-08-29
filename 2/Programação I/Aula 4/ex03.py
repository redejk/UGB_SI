def categoria(i):
    if i >= 5 and i <= 7:
        categoria = ('Infantil A')
        return categoria
    elif i >= 8 and  i <= 10:
        categoria = ('Infantil B')
        return categoria
    elif i >= 11 and i <= 13:
        categoria = ('Juvenil A')
        return categoria
    elif i >= 14 and i <= 17:
        categoria = ('Juvenil B')
        return categoria
    else:
        categoria = ('Adulto')
        return categoria

resultado = categoria(10)
print(f'Sua categoria foi: {resultado}')
