nome = input('Insira um nome: ')

NOME = nome.upper()

nometam = len(nome)

for i in range(nometam):
    print(NOME[nometam - i -1], end='\n')

