# Jogadores
SomaJogadores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
flag = True
while flag:
    numjogador = int(input('Insira um valor entre 1 a 23 para votar nos jogadores respectivos ao número de sua camisa.\nCaso queira sair, digite 0.\n'))
    if numjogador == 0:
        flag = False
    elif numjogador > 23 or numjogador < 0 :
        print('INSIRA UM NÚMERO VÁLIDO.')
    else:
        numjogador = numjogador - 1
        SomaJogadores[numjogador] = SomaJogadores[numjogador] + 1
        print(f'\n=== VOTO COMPUTADO! ===\n')
print(SomaJogadores)
c = 1
total = sum(SomaJogadores)

# Nº Votos por jogador
for i in SomaJogadores:
#   print(f'Jogador número:  {c}: {i} Votos')
    c = c + 1
porcentagem = 0 
for i in range(len(SomaJogadores)): 
    if SomaJogadores[i] != 0:
       # porcentagem = SomaJogadores[i]/total*100
        print(f' { str(i+1).ljust(9)} {str(SomaJogadores[i]).ljust(5)} {(SomaJogadores[i]/total*100):.2f}%')


    
print(f'Foram apurados {total} votos!')

