# IMPORTAR SQLITE 3 - biblioteca padrão python
import sqlite3 

# Cria / acessar / conectar arquivo de tabela
conexao = sqlite3.connect('arquivo.sqlite')

# Cria objeto para executar comandos na conexão SQL
cursor = conexao.cursor()

# Lugar pra colocar o código SQL a ser executado
sql = """ CREATE TABLE IF NOT EXISTS tabela (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
    );
"""

# Executar comandos SQL
cursor.execute(sql) 
cursor.execute(sql, listaOuTupla) 
cursor.execute(sql, [a,b,c]) 
cursor.execute(sql, (a,)) # VIRGULA PARA ELE IDENTIFICAR COMO TUPLA E NÃO UM ELEMENTO INDIVIDUAL

# Pegar elementos pra depois ler
resultado = cursor.fetchall()
print(resultado)

# Salvar permanentemente no banco de dados
conexao.commit()

# Fechar a conexao do arquivo atual com o banco de dados
conexao.close()