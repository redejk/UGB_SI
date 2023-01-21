import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()

p_id = 3

sql = f"""
DELETE FROM clientes
WHERE id = {p_id};
"""

cursor.execute(sql)
conexao.commit()
print('deletado com sucesso...')
conexao.close()