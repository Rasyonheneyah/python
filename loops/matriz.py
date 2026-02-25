matriz = [
    ['nome', 'idade', 'nota'],
    ['pedro', 25, 6],
    ['joao', 22, 4],
    ['henrique', 20, 0.5],

    ]
for i in matriz:
    'if i[2] >= 0:'
    if type(i[2]) != str:
        if i[2] >= 0 and i[2]<10:

            print(i[2]) 

total = 0
for o in range(1, len(matriz)):
    print(matriz[o][2])
    total += matriz[o][2] 
print(f'O total e {total}')
