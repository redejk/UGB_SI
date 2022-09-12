def fat():
    faturamento = 0
    lista_produtos = []
    while True:
        questao = input('CADASTRAR PRODUTO? SIM ou SAIR ?\n')
        if questao.upper() == 'SAIR':
            break
        else:
            quantidade = int(input('Digite a quantidade desse produto: '))
            preco = float(input('Digite o valor desse produto: '))
            lista_produtos.append((quantidade, preco))
    for quantidade, preco in lista_produtos:
        faturamento = faturamento + (quantidade * preco)
    return (f'O total de faturamento desses produtos é: {faturamento}')

faturamento_total= fat()
print(faturamento_total)