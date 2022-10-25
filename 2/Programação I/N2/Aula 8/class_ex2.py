class Gato:
    def __init__(self, cor, peso, pelugem, raca, porte):
        self.cor = cor
        self.peso = peso
        self.pelugem = pelugem
        self.raca = raca
        self.porte = porte

animal = Gato('branca', 7.0, 'liso', 'pitbull', 'grande')
print(f'Meu Gato tem a cor: {animal.cor}\nEle pesa: {animal.peso} kg\nO tipo de pelo é: {animal.pelugem}\nÉ da raça: {animal.raca}\nO porte dele é: {animal.porte}')