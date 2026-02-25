from tank import Tank

tanks = {
    # Key: Value
    'a': Tank('Misael'),
    'b': Tank('Luca'),
    'c': Tank('Apolo')    
}

players = len(tanks)

while players > 1:
    
    for tankName in sorted(tanks.keys()):
        print(f'{tankName} - {(str(tanks[tankName]).center(12))} - {tanks[tankName].alive}')
        
    
    flag = True
    while flag:
        first = input('Quem vai atacar? ').lower() # Pega a key do dicionário TANKS transformando em minúsculo 
        second = input('Quem foi atacado? ').lower() # Pega a key do dicionário TANKS transformando em minusculo tbm
        
        
        if first and second in tanks.keys():
            firstTank = tanks[first]
            secondTank = tanks[second]
            if firstTank.alive and secondTank.alive:
                flag = False
            else:
                print('O alvo precisa estar vivo!')
        else:
            print('Digite usuários válidos!')
    
    firstTank.fire_at(secondTank)
    if not secondTank.alive:
        players -= 1
        print(f'\nUm tanque foi explodido! Restam {players} jogadores!\n') 
for tank in tanks.values():
    if tank.alive:
        print(f'\n\nO vencedor foi {tank.name}!\n\n')


        
    
    
