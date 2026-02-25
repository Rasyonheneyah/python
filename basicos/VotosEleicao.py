# Número de votos totais, brancos, nulos e válidos e o percentual de cada um em relação ao total
print('Vamos analisar as eleições de determinada cidade!')
Total=float(input('Insira o total de votos daquela eleição:'))
Brancos=float(input('Insira o valor de votos brancos daquela eleição:'))
Nulos=float(input('Insira o valor de votos nulos daquela eleição:'))
Validos=float(Total-Brancos-Nulos)
print()
print('Votos Totais =',Total)
print('Votos Válidos =', Validos)
print('Votos Brancos =', Brancos)
print('Votos Nulos =', Nulos)
print()
print('O percentual dos Votos Totais é igual a',(Total/Total)*100,'%')
print('O percentual dos Votos Brancos é igual a',(Brancos/Total)*100,'%')
print('O percentual dos Votos Nulos é igual a',(Nulos/Total)*100,'%')
print('O percentual dos Votos Válidos é igual a',(Validos/Total)*100,'%')



