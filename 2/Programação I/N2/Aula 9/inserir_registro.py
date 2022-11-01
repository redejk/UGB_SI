import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()

p_nome = "Ricardo"
p_idade = 47

sql = '''
INSERT INTO clientes (nome, idade)
VALUES (?, ?);
'''

cursor.execute(sql, (p_nome, p_idade))
conexao.commit()
print('gravado com sucesso...')
conexao.close()