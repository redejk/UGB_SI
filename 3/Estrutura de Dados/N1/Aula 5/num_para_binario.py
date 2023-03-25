from pilha import Pilha
pilha = Pilha()
x = int(input('Digite um numero: '))

while x > 0:
    resto = x % 2
    pilha.empilha(resto)
    x = x // 2

x = ""
while (not pilha.pilhaVazia()):
    x = x + str(pilha.desempilha())

print(x)