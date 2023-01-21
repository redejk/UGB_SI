import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()

sql = """
SELECT * FROM clientes;
"""

cursor.execute(sql)

resultados = cursor.fetchall()

print(resultados)

conexao.close()