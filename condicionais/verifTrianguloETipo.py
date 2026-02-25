A=int(input('Insira o valor de A:'))
B=int(input('Insira o valor de B:'))
C=int(input('Insira o valor de C:'))
#Validação de Triângulo
if A<B + C and B<A+C and C<A+B:
    if A==B and B==C:
        #Verificação Equilátero
        print('O triângulo é Equilátero, pois possui todos os lados iguais.')
    else:
        #Verificação Isóceles
        if A==B or A==C or C==B:
            print('O triângulo é Isóceles, pois possui dois lados iguais')
        else:
            #Verificação se é um triangulo qualquer
            print('É um triângulo qualquer, pois seus três lados são diferentes.')
else:
    print('Não é um triângulo, pois seus lados são irreais.')
        
