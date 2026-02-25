'''
3.Dado um conjunto de palavras [‘fita’, ‘Adenilton’, 
‘armario’, ‘gaveta’, ‘Bruna’, ‘adentro’, ‘folga’, 
‘impressora’]. Montar um filtro que remova todas as 
palavras que comecem com ‘A’ ou ‘a’.
'''
palavras = ['fit', 'Adenilton', 'armario', 'gaveta', 'Bruna', 'adentro', 'folga', 'impressora']

def filtro(palavras):
    nova= []
    for palavra in palavras:
        if palavra[0] != 'A' and \
           palavra[0] != 'a':
            nova.append(palavra)

    return nova
print(filtro(palavras))
