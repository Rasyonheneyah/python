class Personagem:
    def __init__ (self, user):
        self.user = user
        self.alive = True


        print(f'Personagem {self.user} criado!')

    def ifDead(self):
        if self.hp < 1:
            self.alive = False
            print(f'{self.user} is dead.')
    def isAlive(self):
        if self.alive:
            print(f'{self.user} is alive!')
            return True
        else:
            print(f'{self.user} is not alive!')
            return False
    


    def attack(self, target):
        if self.isAlive() and target.isAlive():
            target.hp -= self.damage
            target.isDead()
            print(f'{self.user} causou {self.damage} de dano em {target.user}.\nHP restante: {target.hp}')



class Mage(Personagem):
    def __init__(self, user):
        Personagem.__init__(self, user)
        self.hp = 40
        self.hpmax = self.hp

        self.mana = 100
        self.manaMax = self.mana

        self.damage = 2

        recoveryMana = 15

    def attack(self, target, manaUse):
        if self.isAlive() and target.isAlive():
            if manaUse == self.manaMax:
                target.hp -=  manaUse*5
                target.isDead()
                print(f'{self.user} causou {manaUse*5} de dano em {target.user}\nHP restante: {target.hp}')
            elif manaUse == 0:
                target.hp -= self.damage
                target.isDead()
                print(f'{self.user} causou {self.damage} de dano em {target.user}.\nHP restante: {target.hp}')
            elif manaUse <  self.mana or manaUse < 0:
                print('-- Attack Failed! --')
                target.hp -= 1
                print(f'{self.user} causou -1 de dano em {target.user}.\nHP restante: {target.hp}')
            else:
                target.hp -= (self.damage*manaUse)
                target.isDead()
                print(f'{self.user} causou {self.damage*manaUse} de dano em {target.user}.\nHP restante: {target.hp}')

        

class Warrior(Personagem):
    def __init__(self, user):
        Personagem.__init__(self, user)
        self.hp = 300
        self.hpmax = self.hp

        self.damage = 50

        self.stamina = 100
        self.staminamax = self.stamina

    def heavyAttack(self, target):
        if self.alive and target.alive:
            if self.stamina >= 50:
                target.hp -= (self.damage*3)
                target.isDead()
                self.stamina -= 50
                print(f'{self.user} causou {self.damage*3} de dano em {target.user}.\nHP restante: {target.hp}')



            else: 
                print(f'-- Attack Failed --')
                target.hp -= 1  
                target.isDead()
                print(f'{self.user} causou -1 de dano em {target.user}.\nHP restante: {target.hp}')

                

    def colossalStrike(self, target):
        if self.alive and target.alive:
            if self.stamina == self.staminaMax:
                target.hp -= (self.damage*8)
                target.isDead()
                print(f'{self.user} causou {self.damage*8} de dano em {target.user}.\nHP restante: {target.hp}')




class Assassin(Personagem): 
    def __init__(self, user):
        Personagem.__init__(self, user)
        self.hp = 50
        self.hpMax = self.hp

        self.damage = 40
        
        self.energy = 50
        self.energyMax = self.energy

    def backstab(self, target):
        if self.alive and target.alive:
            if self.energy == self.energyMax:
                damage = (target.hp*0.5) + (self.damage*3)
                target.hp-= damage
                target.isDead()
                print(f'{self.user} causou {self.damage*8} de dano em {target.user}.\nHP restante: {target.hp}')

            elif self.energy <= 0:
                print('-- Atack failed! -- ')
                target.hp-= 1
                target.isDead()
                print(f'{self.user} causou -1 de dano em {target.user}.\nHP restante: {target.hp}')

    def sneakAttack(self, target):
        if self.alive and target.alive:
            if self.energy >= 25:
                damage = (target.hp*0.1) + (self.damage*2)
                target.hp-= damage
                self.energy -= 25
                target.isDead()
                print(f'{self.user} causou {self.damage*8} de dano em {target.user}.\nHP restante: {target.hp}')

            elif self.energy <= 0:
                print('-- Atack failed! -- ')
                target.hp-= 1
                target.isDead()
                print(f'{self.user} causou -1 de dano em {target.user}.\nHP restante: {target.hp}')








