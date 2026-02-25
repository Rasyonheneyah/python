print('Vamos ver se você acerta qual número específico eu tenho armazenado no meu sistema! Chute de 1 a 10! ')
n = int(input('Insira o seu chute aqui!'))
print('')
while n>10 or n<0:
    n = int(input('Insira outro valor, esse não está dentro das regras.'))
acertou=7
if n==acertou:
    print('Parabéns, você acertou! O valor armazenado no meu sistema era ', acertou, '!')
else:
    print('Não foi dessa vez :[ ')
print('Espero que tenha gostado!')