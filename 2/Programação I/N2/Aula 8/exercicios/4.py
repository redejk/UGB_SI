class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso = self.peso + peso

    def emagrecer(self, peso):
        self.peso = self.peso - peso
    
    def crescer(self, altura):
        self.altura = self.altura + altura
    
pessoa = Pessoa('Carlos', 29, 78, 177)
pessoa.envelhecer()
print(f'Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nPeso: {pessoa.peso}\nAltura: {pessoa.altura}')
