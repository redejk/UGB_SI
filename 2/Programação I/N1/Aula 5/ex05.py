media = 0
total = []
while True:
    nome = input("Digite seu nome: ")
    if nome.lower() == 'sair':
        break
    else:
        nt1 = float(input("Digite sua nota 1: "))
        nt2 = float(input("Digite sua nota 2: "))
        total.append((nome, nt1, nt2))

for i in total:
    nome = i[0]
    media = (i[1] + i[2])/2
    if media >= 7.0:
        print(f'{nome} ficou com media: {media} e foi aprovado\n')
    else:
        print(f'{nome} ficou com media: {media} e foi reprovado\n')