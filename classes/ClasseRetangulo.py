class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def mudarLados(self, novoComprimento, novaLargura):
        self.comprimento = self.novoComprimento 
        self.largura = self.novaLargura
        print('Tamanho atualizado!')
    def retornarLados(self):
        return (self.comprimento, self.largura)
    def calcArea(self):
        return self.comprimento*self.largura
    def calcPerimetro(self):
        return (self.comprimento*2)+(self.largura*2)
    
def calcConstrucao():
    print('Vamos medir os rodapés e os pisos necessários para a sua construção! Responda corretamente abaixo.')
    medidas = []
    comprimento = float(input('Insira o comprimento do local: '))
    medidas.append(comprimento)
    largura = float(input('Insira a largura do local: '))
    medidas.append(largura)
    construcao = Retangulo(medidas[0], medidas[1])
    tamPisos = float(input('Insira o tamanho dos pisos: '))
    tamRodapes = float(input('Insira o tamanho dos rodapés: '))
    print(f'Você precisará de {construcao.calcArea()/tamPisos} pisos.')
    print(f'Você precisará de {construcao.calcPerimetro()/tamRodapes} rodapés.')


calcConstrucao()