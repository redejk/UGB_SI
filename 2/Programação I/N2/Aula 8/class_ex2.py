class Gato():
    def __init__(self, cor, peso, pelugem, raca, porte):
        self.cor = cor
        self.peso = peso
        self.pelugem = pelugem
        self.raca = raca
        self.porte = porte

animal = Gato('branca', 7.0, 'liso', 'pitbull', 'grande')
print(f'Meu Gato tem a cor: {animal.cor}')
print(f'Ele pesa: {animal.peso} kg')
print(f'O tipo de pelo é: {animal.pelugem}')
print(f'É da raça: {animal.raca}')
print(f'O porte dele é: {animal.porte}')