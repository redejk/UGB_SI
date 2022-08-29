def media_final(m):
    if m >= 0.0 and m <= 4.9:
        conceito = ('D')
        return conceito
    elif m >= 5.0 and m <= 6.9:
        conceito = ('C')
        return conceito
    elif m >= 7.0 and m <= 8.9:
        conceito = ('B')
        return conceito
    else:
        conceito = ('A')
        return conceito

resultado = media_final(8.5)
print(f'Seu conceito foi: {resultado}')