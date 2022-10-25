class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.__cor = cor
        
    def mostraCor(self):
        print(self.__cor)

    def retornarCor(self):
        return self.__cor

bola = Bola('Azul', 5, 'couro')
bola.mostraCor()
bola.trocaCor('Vermelho')
bola.mostraCor()
print(bola.retornarCor())
