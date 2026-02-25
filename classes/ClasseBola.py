class Bola:
    def __init__ (self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def trocaCor(self, novacor):
        self.novacor = novacor
        self.cor = novacor
    def mostrarCor(self):
        print(self.cor)

# Teste
bola1 = Bola('Azul', 3.14, "Chumbo")
print(f'Cor inicial {bola1.cor}.')
bola1.trocaCor("Verde")
print(f'Cor final {bola1.cor}.')