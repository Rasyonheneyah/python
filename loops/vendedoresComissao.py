vendedores = []
flag = True
while flag:
    salario = int(input('Insira o valor do salário do vendedor: '))
    if salario >= 200:
        vendedores.append(salario)
    else:
        if salario == 0:
            flag = False
        
    
dinfixo = 200

'dsemanal = 200+ 1.09 * '
faixa = [
    (200 ,299 ),
    (300 , 399),
    (400 , 499),
    (500 , 599),
    (600 ,699 ),
    (700 ,799),
    (800 ,899 ),
    (900, 999),
    (1000)


    ]
soma = [0 , 0, 0, 0, 0, 0, 0, 0, 0]
for v in vendedores:
    print(v)
    for i in range(8):
        'print(f[0], f[1])'
        if faixa[i][0] <= v <= faixa[i][1] :
            soma[i] += 1
    if v >= 1000:
        soma[8] +=1

for i in range(9):
    print(f'{faixa[i][0]} - {faixa[i][1]} : {soma[i]} \n')
