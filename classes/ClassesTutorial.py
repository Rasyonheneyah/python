class Vida:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrarNome(self):
        print(self.nome)

    def Falar(self, lingua):
        self.lingua = lingua
        print(self.lingua)
        # LINGUA PRECISA ESTAR REGISTRADO EM UM ATRIBUTO

class Pessoa(Vida):
    def __init__(self, nome, idade, pet):
        Vida.__init__(self, nome, idade)
        self.pet = pet

    def estimacao(self, obj):
        print(obj.nome, obj.idade, obj.dono)

    __vivo = True
    #  dois anderline __ permite você só pegar o 
    # Atributo (variável) só funciona com métodos (função)
    def tavivo(self):
        print(self.__vivo)

class AnimalDomestico(Vida):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        #SUPER PRECISA TIRAR O SELF 
        self.dono = "Misael"
    

    cela = True

# Isso daqui tá fora da classe
# As Classes estão na Memória

Misael = Pessoa('Misael', 19, True)

cav = AnimalDomestico('Cavalo', 18)

print(Misael.nome, Misael.pet, Misael.idade)
print(cav.nome, cav.idade)
Misael.Falar('Oi')

Misael.estimacao(cav)
Misael.tavivo()


Misael.nome = 'Brendo'
# Se a variável é pública vocÊ pode alterá-la facilmente.
Misael.__vivo = False
# Aqui o python considerou "Misael.__vivo " como variável tudo.
# A variável "Misael.__vivo " virou booleano
# O atributo .__vivo da classe Pessoa não mudou internamente, mas você criou uma variável externa

Misael.tavivo()
