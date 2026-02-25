'Salto a distancia cada atelta tem 5 saltos.'
ordem_saltos = {
    0: 'Primeiro',
    1:'Segundo',
    2:'Terceiro',
    3:'Quarto',
    4:'Quinto',
}


atlnome = input('Insira o nome do atleta: ')
saltos = []
for i in range(5):
    salto = float(input(f'Valor do {ordem_saltos[i]} salto: '))
    saltos.append(salto)
print('Carregando...')
print(f'Atleta: {atlnome}')
for i in range(5):
    print(f'{ordem_saltos[i]} salto: {saltos[i]} m')

txt1 = ''

for i in saltos:
    txt1 = txt1 + f'{i} - '

media = sum(saltos)/len(saltos)    
print(f'\nResultado Final: \nAtleta: {atlnome}\nSaltos: {txt1[:-3]}\nMédia: {salto}')
print(media)
