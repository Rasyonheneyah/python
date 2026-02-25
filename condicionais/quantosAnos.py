print('Vou descobrir quantos anos você tem!')
atual=int(input('Digite em que ano estamos atualmente:'))
nasceu=int(input('Digite em que ano você nasceu:'))
idade=atual-nasceu
aniversario=input('Você fez aniversário nesse ano? [S/N]')
if aniversario == 'N':
    idade=idade-1

print('Você tem', idade,'anos!')
