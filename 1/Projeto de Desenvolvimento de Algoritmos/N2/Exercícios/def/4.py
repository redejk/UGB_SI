import random

def inicio():
    nome = input("Digite seu nome: ")
    print(f"Seja bem vindo {nome}, esse é um jogo de adivinhação. \nvocê possui 10 tentativas para descobrir qual é o número sorteado pelo programa! \nVamos começar!")
    tentativa()

def sorteio():
    sorteado = random.randint(1,200)
    return sorteado

def palpite_usuario():
    palpite = int(input("Digite um valor entre 1 e 200: "))
    return palpite

def tentativa():
        cont = 1
        numero_sorteado = sorteio()
        while cont <=10:
            palpite = palpite_usuario()
            if palpite == numero_sorteado:
                print("Parabéns, você adivinhou o número sorteado!!!")
                cont = 11
            else:
                tentativas = 10 - cont
                if palpite < numero_sorteado:
                    print(f"O valor digitado é menor do que o número sorteado, você ainda possui {tentativas} tentativa(s)")
                else:
                    print(f"O valor digitado é maior do que o número sorteador, você ainda possui {tentativas} tentativa(s)")
                cont = cont + 1
                if cont > 10:
                    print(f"Acabou suas tentativas!\nO número sorteado foi {numero_sorteado}")
            
inicio()