class Quadrado:
    def __init__ (self, tamanho):
        self.tamanho = tamanho
    def mudarTamanho(self, novoTamanho):
        self.novoTamanho = novoTamanho
        self.tamanho = novoTamanho
    def valorLado(self):
        return self.tamanho
    def calcArea(self):
        return self.tamanho*4

# TESTE
quad1 = Quadrado(10)
print(f'Cada lado é {quad1.valorLado()}')
quad1.mudarTamanho(5)
print(f'Cada lado agora é {quad1.valorLado()}')
print(f'A área é igual a {quad1.calcArea()}')