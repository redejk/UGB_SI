class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
    def retornar_valor_lado(self):
        return self.tamanho_lado
    
    def calcular_area(self):
        return self.tamanho_lado * self.tamanho_lado

valor = float(input("Entre com o lado do quadrado: "))
quadrado = Quadrado(valor)
print(quadrado.calcular_area())

novo_valor = float(input("Entre com outro valor para o lado do quadrado: "))
quadrado.mudar_valor_lado(novo_valor)
print(quadrado.calcular_area())
