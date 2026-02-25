'''
Exercício 5:
Construa um algoritmo capaz de permitir a entrada, via
teclado, do nome do aluno e suas duas notas até que o nome
sair aparecer e terminar o programa. No final deverá
apresentar o nome e a média das notas junto com mensagem
aprovado (>=7) ou reprovado (<7)
'''

valores = []
while True:
    
    nome = input('Insira o nome: ')
    if nome.lower() == 'sair':
        break
    else:
        
        notas = []
        for i in range(2):
            nota = float(input(f'Nota {i+1} : '))
            
            notas.append(nota)

        
        valores.append((nome, notas))
print(valores)

for nome, nota in valores:
    media = sum(nota)/len(nota)
    print(nome)
    if (media>=7):
        print( 'Aprovado')
    else:
        print('reprovado')
