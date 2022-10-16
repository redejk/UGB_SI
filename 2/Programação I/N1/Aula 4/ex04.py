def verifica_numero(a):
    if a > 0:
        return True
    elif a < 0:
        return False
    else:
        return None

resultado = verifica_numero(5)
print(resultado)