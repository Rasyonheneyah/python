# valor do pagamento
"""
1.Faça um programa que use a função valorPagamento 
para determinar o valor a ser pago por uma prestação 
de uma conta. O programa deverá solicitar ao usuário 
o valor da prestação e o número de dias em atraso e 
passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor 
ao programa que a chamou. O programa deverá então 
exibir o valor a ser pago na tela. Após a execução o 
programa deverá voltar a pedir outro valor de prestação 
e assim continuar até que seja informado um valor igual 
a zero para a prestação. Neste momento o programa 
deverá ser encerrado, exibindo o relatório do dia, que 
conterá a quantidade e o valor total de prestações 
pagas no dia. O cálculo do valor a ser pago é feito da 
seguinte forma. Para pagamentos sem atraso, cobrar o 
valor da prestação. Quando houver atraso, cobrar 3% 
de multa, mais 0,1% de juros por dia de atraso
"""

pag = []
pagAdd = []
diapag = ['dia','pagamento']
def input_pagamento():
    flag = True
    while flag:
        if flag == True:
            for i in diapag:
              pagAdd = float(input(f'Insira {i}: '))
              
            pag.append(pagAdd)
            print(pag)

                  
        encerrar = input('Você deseja encerrar? S/N')
        if encerrar = 'S'
            flag = False

        
def valor_pagamento(valor, dias):
    if dias !=0:
        valor = valor + (valor*0.03)
        for i in range(dias):
            valor = (valor * 1.001)

    return valor
