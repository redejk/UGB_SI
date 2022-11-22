from crud import MyCrud
crud = MyCrud()

crud.criarTabela()

while True:
    print("""
    Escolha uma opção:
    1 - Incluir
    2 - Ler
    3 - Alterar
    4 - Deletar
    5 - Sair
    """)
    valor = input('-->')
    if valor == '1':
        nome = input('Digite um nome: ')
        while True:
            cpf = input('Digite o cpf: ')
            if len(cpf) != 11:
                print('O cpf deve ter 11 digitos e ser digitado sem ponto ou hífen')
            else:
                break
        crud.inserir(nome, cpf)
    elif valor == '2':
        crud.selecionar()
    elif valor == '3':
        id = int(input("Digite o ID que deseja alterar: "))
        nome = input('Digite o nome: ')
        while True:
            cpf = input('Digite o cpf: ')
            if len(cpf) != 11:
                print('O cpf deve ter 11 digitos e ser digitado sem ponto ou hífen')
            else:
                break
        crud.alterar(id, nome, cpf)
    elif valor =='4':
        id = int(input('Digite o ID que deseja deletar: '))
        crud.deletar(id)
    else:
        break
