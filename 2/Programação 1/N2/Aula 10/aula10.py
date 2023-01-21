from crud import MyCrud

mycrud = MyCrud('teste.db')
mycrud.create_table('clientes', 'nome', 'cpf')
mycrud.insert('Carlos', '421.143.298-28')
print(mycrud.select())
mycrud.update('clientes', 'nome', 'cpf', 1, 'Pedro', '111.111.111-11')
print(mycrud.select())
mycrud.delete('clientes', '1')
print(mycrud.select())