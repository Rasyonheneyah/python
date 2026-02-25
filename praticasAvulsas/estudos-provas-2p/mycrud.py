class myCrud:
    def __init__(self, nomeArquivo):
        import sqlite3 

        self.conexao = sqlite3.connect(f'{nomeArquivo}.sqlite')
        self.cursor = self.conexao.cursor()

        print('CLASSE INSTANCIADA')

    def create(self, dados):
        sql = f"""CREATE TABLE IF NOT EXISTS {self.dados['tabela']}(\nid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT\n """
        for campo in self.dados['campos']:
            sql = f'{campo} {self.dados['campos'][campo], }'
        sql = sql[:-2] + ')'

        self.cursor.execute(sql)
        self.conexao.commit()

        print('Tabela Criada')

    def read(self, dados):
        sql = f'SELECT '
        for campo in self.dados['campos']:
            sql += f'{self.dados['campos'][campo]}, '
        
        sql = sql[:-2] + f' FROM {self.dados['tabela']};' 

        
    def close(self):
        self.cursor.close()

