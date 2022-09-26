def par_impar(n):
    if n % 2 == 0:
        return True
    else:
        return False

valores = [4, 6, 2, -8, 9, -12]
for valor in valores:
    print(valor, par_impar(valor))