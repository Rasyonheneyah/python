'''
 Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e informações como: se o valor é um número,
 se a variável começa com a primeira letra maiúsculas.
'''

tecla = input('Digite alguma tecla:  ')
def mostrartipo(carac):
    type(carac)
    if type(carac) == float:
        print('É um número float.')
    elif carac.isdigit()== int:
        print('É um inteiro.')
    elif type(carac) == bool:
        print('É um booleano.')
    else:
        print('É uma string.')
        if carac[0]== carac[0].upper:
            print('Começa com maiúscula.')
        else:
            print('Começa com minúscula.')
mostrartipo(tecla)
mostrartipo('String')
mostrartipo(5)
mostrartipo(True)
mostrartipo(0.5)
