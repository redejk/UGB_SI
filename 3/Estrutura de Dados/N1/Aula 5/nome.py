from pilha import Pilha
pilha = Pilha()
nome = input('Digite seu nome: ')
for i in nome:
    pilha.empilha(i)
x = ""
while (not pilha.pilhaVazia()):
    x = x + pilha.desempilha()

print(x)