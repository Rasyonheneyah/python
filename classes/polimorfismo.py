class player:
    def __init__(self, id, nome, genero):
        self.id = id
        self.nome = nome
        self.genero = genero

        self.level = 1
        self.perks = 3
    
    def ganharXp(self):
        level = self.level
        levelAtual = level 
        self.level = level + level/100
        if int(levelAtual + 1) == level: 
            self.perks = self.perks + 3
            print(f'Parabéns! {self.nome}, você subiu para o nível ${level}. \nAgora você tem {self.perks} perks disponíveis para utilizar! ')
        else:
            print(f'XP atual: {self.level}')

    def move(self):
        print('Você se moveu!')

    def atacar(self, multplicador):
        ataque = int(self.level) * self.multiplicador
        

class guerreiro(player):
    def __init__(self, id, nome, genero, reliquia):
        # super().__init__(id, nome, genero)
        player.__init__(self, id, nome, genero)

        self.forca = 20
        self.estamina= 16
        self.magia = 6
        self.fe = 8
        self.inteligencia = 11

        self.inv += self.reliquia
        self.multiplicador = self.forca

class mago(player):
    def __init__(self, id, nome, genero, reliquia):
        super().__init__(id, nome, genero)
        
        self.forca = 9
        self.estamina= 12
        self.magia = 20
        self.fe = 6
        self.inteligencia = 16

        self.inv += self.reliquia
        self.multiplicador = self.magia
