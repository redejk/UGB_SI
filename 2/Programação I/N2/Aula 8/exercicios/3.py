class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudar_valor_lados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def retornar_valor_lados(self):
        return self.ladoA, self.ladoB
    
    def calcular_area(self):
        return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        return (self.ladoA + self.ladoB) * 2
    
ladoA = float(input("Digite o valor do lado A: "))
ladoB = float(input("Digite o valor do lado B: "))
tamanho_piso = float(input("Digite o tamanho do piso: "))
retangulo = Retangulo(ladoA, ladoB)
area = retangulo.calcular_area()
quantidade_pisos = (area) / (tamanho_piso)
print(f'A area é: {retangulo.calcular_area()}\nO perimetro é: {retangulo.calcular_perimetro()}')
print(f'Será necessário utilizar {round(quantidade_pisos)} pisos para completar a área')
