""" Nome: Carlos Eduardo Ferreira 2022101225
Trabalho de Prog. 2º 
22/11/2022
"""

class MyCrud:
    def __init__(self):
        import sqlite3
        self.conexao = sqlite3.connect('moleza.sqlite')
        self.cursor = self.conexao.cursor()
    
    def fecharDB(self):
        self.conexao.close()

    def criarTabela(self):
        sql = """
            create table if not exists pessoas(
                id integer not null primary key autoincrement,
                nome text not null,
                cpf text caracter (11)
            );
        """
        self.cursor.execute(sql)
        print('Tabela criada...')

    def selecionar(self):
        sql = """
            select * from pessoas;
        """
        resultado = self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for i in resultado:
            print(i)

    def inserir (self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        sql = f"""
            insert into pessoas (nome, cpf)
            values('{nome}', '{cpf}');
        """
        self.cursor.execute(sql)
        self.conexao.commit()
        print('Salvo com sucesso...')

    def alterar(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        sql = f"""
            update pessoas
            set nome = '{self.nome}', cpf = '{self.cpf}'
            where id = {self.id};
        """
        self.cursor.execute(sql)
        self.conexao.commit()
        print('alterado com sucesso...')

    def deletar(self, id):
        self.id = id
        sql = f"""
            delete from pessoas
            where id = {self.id};
        """
        self.cursor.execute(sql)
        self.conexao.commit()
        print('deletado com sucesso...')