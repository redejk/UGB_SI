from crud import MyCrud

my_crud = MyCrud('cliente.sqlite3')
my_crud.criarTabela()
results = my_crud.selecionar()
for result in results:
    print(result)

dados = {
    'tabela': 'fornecedor',
    'campos': ['nome', 'cnpj'],
    'valores': ['nota', 20]
}

my_crud.inserir(dados)
print(my_crud.selecionar())

my_crud.alterar(3, 'pedro', 18)
my_crud.deletar(4)
print(my_crud.selecionar())

my_crud.fecharDB()