""" 
1. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
Fevereiro, . . . ).
"""
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp=[]
mediaA = 0
n = 12
def tempmedia(mediaA):

    for i in range(n):
        tp = float(input(f'Insira a temperatura de {meses[i]}: '))
        temp.append(tp)
        mediaA = tp + mediaA


    print("Temperatura acima da média anual")
    mediaA = mediaA/len(meses)
    print(mediaA)
    for i in range(n):
        if temp[i] > mediaA:
            print(f'{meses[i]} -> {temp[i]}°')
        

tempmedia(mediaA)

