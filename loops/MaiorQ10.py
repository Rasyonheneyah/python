# Números maiores que 10
valor=int(input('Insira um valor:')) 
while valor==10:
    valor=int(input('Insira outro valor:'))
    continue
if valor>10 and valor!=10:
    print('O número', valor, 'é maior que 10.')
else:
    valor!=10
    print('O número', valor, 'é menor que 10.')