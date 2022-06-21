def par_ou_impar():
    x = 0
    while x <=10:
        x = int(input("Digite um numero: "))
        if x % 2 == 0:
            print("par")
        else:
            print("impar")

par_ou_impar()