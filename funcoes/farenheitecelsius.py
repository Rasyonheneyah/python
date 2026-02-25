'''
5.Escreva um script que pergunta ao usuário se ele 
deseja converter uma temperatura de grau Celsius para
Farenheit ou vice-versa. Para cada opção, crie uma 
função. Crie uma terceira, que é um menu para o 
usuário escolher a opção desejada, onde esse menu 
chama a função de conversão correta.

'''

def cel_far(c):
    f = (c *1.8) +32
    return f
def far_cel(f):
    c = (f-32)/1.8
    return c


def menu():
    print("""
1- Converter Celsius para Farenheit
2- Converter Farenheit para Celsius
3- Sair
""")
    opcao = int(input('Digite um número -> '))
    if opcao ==1:
        c = float(input('Celsius: '))
        print(cel_far(c))
    elif opcao ==2:
        f = float(input('Fahrenheit: '))
        print(far_cel(f))
    
    else:
      pass  

menu()
