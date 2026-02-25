# Verificador se o número e positivo.
num=int(input('Insira um número:'))
if num>0:
    quale= 'Número Positivo'
else:
    if num<0:
        quale='Número Negativo'
    else:
        quale='Zero'
print(quale)
