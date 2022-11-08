import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()

p_nome = "Ricardo"
p_idade = 47

sql = f"""
INSERT INTO clientes (nome, idade)
VALUES ('{p_nome}', {p_idade});
"""

cursor.execute(sql)
conexao.commit()
print('gravado com sucesso...')
conexao.close()