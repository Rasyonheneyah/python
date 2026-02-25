class Tank:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60
    
    def __str__(self):
        if self.alive: #Se o alive tiver True
            return f'{self.name} ({self.armor} armor, {self.ammo} shells )'

        else:
            return f'{self.name} (MORTO)'
    
    def fire_at(self, enemy):
        if self.name != enemy.name:    
            if self.alive and self.ammo>=1 and enemy.alive:
                self.ammo-=1
                print(f'{self.name} disparou contra {enemy.name}! ')
                enemy.hit()
            elif not self.alive:
                print(f'{self.name} foi explodido!')
            else: 
                print(f'{self.name} não tem munição!')
        else:
            print('Você não pode atirar em si mesmo!')
    def hit(self):
        self.armor -= 20
        print(f'{self.name} foi atingido!')
        if self.armor <= 0:
            self.explode()
    
    def explode(self):
        self.alive = False
        print(f'BOOM! {self.name} explodiu!')


            
            






