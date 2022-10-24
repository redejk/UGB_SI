class Copo:
    def __init__(self, cor, altura, material):
        self.cor = cor
        self.altura = altura
        self.material = material

copo_plastico = Copo('branco', 7.5, 'plastico')
print(f'Cor: {copo_plastico.cor}')
print(f'Altura: {copo_plastico.altura}')
print(f'Material: {copo_plastico.material}')
print('****************************')

copo_metal = Copo('Cinza', 8, 'metal')
print(f'Cor: {copo_metal.cor}\nAltura: {copo_metal.altura}\nMaterial: {copo_metal.material}')