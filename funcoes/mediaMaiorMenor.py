'''
6.Faça um programa, com uma função que necessite de 
três argumentos, e que forneça a soma desses três 
argumentos através de uma função. Seu script também 
deve fornecer a média dos três números, através de 
uma segunda função que chama a primeira.
'''

def soma(*args):
    soma = sum(args)
    return soma

def media(*args):
    return sum(args)/len(args)

def tres(a, b, c):
    print(soma(a,b,c))
    print(f'Média: {media(a,b,c)}')


    print(maior(a, b, c))
    print(menor(a, b ,c))

'''
7.Faça um programa que recebe três números do usuário, 
e identifica o maior através de uma função e o menor 
número através de outra função.
'''

def maior(*args):
    nmaior = args[0]
    '''
    for i in args:
        if i > nmaior:
            nmaior = i
    print(f'Maior: {nmaior}')
    '''
    return max(args)
    
def menor(*args):
    nmenor = args[0]
    

    '''
    for i in args:
        if i < nmenor:
            nmenor = i
    print(f'Menor: {nmenor}')
    '''    
    return min(args)
tres(1,2,3)
