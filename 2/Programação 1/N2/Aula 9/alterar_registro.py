import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()

nome_update = 'Larissa'
idade_update = 18
p_id = 3

sql = f"""
UPDATE clientes
SET nome = '{nome_update}', idade = {idade_update}
WHERE id = {p_id};
"""



cursor.execute(sql)
conexao.commit()
print("alterado com sucesso...")
conexao.close()