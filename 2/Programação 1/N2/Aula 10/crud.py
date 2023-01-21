class MyCrud:
    def __init__(self, db):
        import sqlite3
        self.conexao = sqlite3.connect(db)
        self.cur = self.conexao.cursor()

    def close_db(self):
        self.conexao.close()
        print('conexão fechada')

    def create_table(self, tb_name, coluna1, coluna2):
        self.tb_name = tb_name
        self.coluna1 = coluna1
        self.coluna2 = coluna2
        sql = f"""
        CREATE TABLE IF NOT EXISTS {self.tb_name} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            {self.coluna1} TEXT NOT NULL,
            {self.coluna2} TEXT
            )"""
        self.cur.execute(sql)
        self.conexao.commit()
        print('tabela criada')

    def select(self):
        sql = """
        SELECT * FROM clientes"""
        self.cur.execute(sql)
        resultado = self.cur.fetchall()
        for i in resultado:
            print(i)

    def insert(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        sql = f"""
        INSERT INTO clientes (nome, cpf) VALUES ('{self.nome}', '{self.cpf}')"""
        self.cur.execute(sql)
        self.conexao.commit()
        print('Dados inseridos')

    def update(self, tb_name, coluna1, coluna2, id, dados_coluna1, dados_coluna2):
        self.tb_name = tb_name
        self.coluna1 = coluna1
        self.coluna2 = coluna2
        self.id = id
        self.dados_coluna1 = dados_coluna1
        self.dados_coluna2 = dados_coluna2
        sql = f"""UPDATE {self.tb_name}
        SET {self.coluna1} = "{self.dados_coluna1}", {self.coluna2} = "{self.dados_coluna2}"
        WHERE id = {self.id}"""
        self.cur.execute(sql)
        self.conexao.commit()
        print('Dados alterados')

    def delete(self, tb_name, id):
        self.tb_name = tb_name
        self.id = id
        sql = f"""
        DELETE FROM {tb_name}
        WHERE id = '{self.id}'"""
        self.cur.execute(sql)
        self.conexao.commit()
        print('Dado deletados')