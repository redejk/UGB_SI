from crud_firebase import CrudFirebase
crud = CrudFirebase()

while True:
    print("""
    Escolha uma opção:
    1 - Incluir
    2 - Ler
    3 - Alterar
    4 - Deletar
    5 - Ler Alunos
    6 - Sair
    """)
    valor = input("-->")
    if valor == '1':
        chave = input('Digite sua matrícula: ')
        nome = input('Entre com seu nome: ')
        comida = input('Entre com a comida preferida: ')
        dados = {
            'nome' : nome,
            'comida' : comida
        }
        crud.incluirDB(chave, dados)
    elif valor == '2':
        chave = input('Digite sua matrícula: ')
        resultados = crud.lerDB(chave)
        for resultado in resultados:
            print(resultado.key())
            print(resultado.val())
    elif valor == '3':
        chave = input('Digite sua matrícula: ')
        nome = input('Digite seu nome: ')
        comida = input('Digite sua comida preferida: ')
        dados = {
            'nome' : nome,
            'comida' : comida
        }
        crud.alterarDB(chave, dados)
    elif valor == '4':
        chave = input('Digite sua matrícula: ')
        crud.deletarDB(chave)
    elif valor == '5':
        chave = ''
        resultados = crud.ler_alunos(chave)
        for resultado in resultados:
            print(resultado.key())
            print(resultado.val())
    else:
        break
