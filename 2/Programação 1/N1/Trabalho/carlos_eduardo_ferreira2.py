def fat():
    faturamento = 0
    lista_produtos = []
    while True:
        questao = input('CADASTRAR PRODUTO? SIM ou SAIR ?\n')
        if questao.upper() == 'SAIR':
            break
        else:
            nome = input('Digite o nome do produto: ')
            quantidade = int(input('Digite a quantidade desse produto: '))
            preco = float(input('Digite o valor desse produto: '))
            lista_produtos.append((nome, quantidade, preco))
    for i in lista_produtos:
        quantidade = i[1]
        preco = i[2]
        faturamento = faturamento + (quantidade * preco)
    return (f'O total de faturamento desses produtos é: {faturamento}')

print(fat())