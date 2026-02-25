class Animal:
  def __init__(self, nome):
    self.nome = nome
class Gato(Animal):
  def miar(self):
    print("Miau miau!")

Gato('Garfield').miar()