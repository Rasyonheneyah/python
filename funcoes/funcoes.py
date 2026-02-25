'''
def soma(*args):
    return sum(args)
print(soma(2,3,4,5,9,8,74,20,-5))

def nomes(**kwargs):
    return kwargs['nome']
resultado = nomes(nome = 'Misael', idade = 51)
print(resultado.upper())
'''

def namelist(lista):
    b = lista#.copy() precisa do .copy para você não mexer na lista 
    b.append(7)
    return b
    
l = [1,3,5]
r = namelist(l)
print(r)
print(l)
# Não dá pra dar print(b) pq a variável B está fora de escopo
# Se você igualar listas, quando você mexe em um, mexe no outro.
