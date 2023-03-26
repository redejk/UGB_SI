from pilha import Pilha
pilha = Pilha()
x = int(input('Digite um numero: '))

while x > 0:
    resto = x % 2
    pilha.push(resto)
    x = x // 2

x = ""
while (not pilha.pilhaVazia()):
    x = x + str(pilha.pop())

print(x)