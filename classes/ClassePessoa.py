"""
4. Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que
nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, maisIdade):
        if self.idade<21:
            # A altura da pessoa é igual a sua idade acrescentada (if -21 anos)
            self.altura = (self.maisIdade*0.5) + self.altura
        self.idade = self.idade+ self.maisIdade
        return self.idade
    def engordar(self, pesoMais):
        self.peso = self.peso + self.pesoMais
        return self.peso
    def emagrecer(self, pesoMenos ):
        self.peso = self.peso - self.pesoMenos
        return self.peso
    

    