matriz = [
    ['andre', 3, 5, 6],
    ['joao', 4, 2, 9],
    ['pedro', 9, 7, 5],
    ['jose', 1, 1, 1]
]
for l in range(len(matriz)):
    soma = 0
    for c in range(1, len(matriz[l])):
        soma = soma + matriz[l][c]
    print(f'O aluno {matriz[l][0]} teve uma soma de notas igual a {soma}')