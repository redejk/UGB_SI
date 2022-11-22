class MyCrud:

    def __init__(self, banco):
        import sqlite3
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def fecharDB(self):
        self.conexao.close()

    def criarTabela(self):
        sql = '''
            create table if not exists clientes(
                id integer not null primary key autoincrement,
                nome text not null,
                idade integer
            );
        '''
        self.cursor.execute(sql)
        print('Tabela criada...')

    def selecionar(self):
        sql = '''
            select * from clientes;
        '''
        resultado = self.cursor.execute(sql)
        return resultado.fetchall()

    def inserir (self, dados):
        campos = '('
        for i in dados['campos']:
            campos += f'{i}, '
        campos = f'{campos[:-2]})'
        print(dados['tabela'])
        print(campos)
        sql = f'''
            insert into {dados['tabela']}{campos}
            values(?, ?);
        '''
        print(sql)
        # self.cursor.execute(sql, [nome, idade])
        # self.conexao.commit()
        print('Salvo com sucesso...')

    def alterar(self, id, nome, idade):
        sql = '''
            update clientes
            set nome = ?, idade = ?
            where id = ?;
        '''
        self.cursor.execute(sql, [nome, idade, id])
        self.conexao.commit()
        print('alterado com sucesso...')

    def deletar(self, id):
        sql = '''
            delete from clientes
            where id = ?;
        '''
        self.cursor.execute(sql, [id])
        self.conexao.commit()
        print('deletado com sucesso...')