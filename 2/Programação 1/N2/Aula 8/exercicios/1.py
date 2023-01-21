class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor
        
    def mostraCor(self):
        print(self.cor)

    def retornarCor(self):
        return self.cor

bola = Bola('Azul', 5, 'couro')
bola.mostraCor()
bola.trocaCor('Vermelho')
bola.mostraCor()
print(bola.retornarCor())
