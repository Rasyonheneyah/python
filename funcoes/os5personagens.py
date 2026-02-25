print('Crie 5 personagens através das mensagens abaixo.')
def caracteristicas_personagens():
    nome = input('Digite o nome do personagem:')
    idade=input('Digite a idade do personagem:')
    origem=input("Digite o local de origem do personagem:")
    corfavorita=input("Digite a cor favorita desse personagem:")
    missao=input('Digite a sua missão')
    print('O ', nome,' tem ', idade, ' anos, nasceu no(a)', origem,' sua cor favorita é ', corfavorita, ', sua missão é ', missao)
tempo=5
while tempo!=0: 
    caracteristicas_personagens()
    
    tempo=tempo-1
