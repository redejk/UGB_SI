import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()


sql = """
UPDATE clientes
SET nome = ?, idade = ?
WHERE id = ?;
"""

nome_update = 'João'
idade_update = 20
p_id = 1

cursor.execute(sql, (nome_update, idade_update, p_id))
conexao.commit()
print("alterado com sucesso...")
conexao.close()