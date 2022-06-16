resposta = 'SIM'
soma = 0
while (resposta != 'NÃO') and (resposta != 'não'):
    comodo = input("Digite o nome do cômodo: ")
    largura = float(input("Digite a largura em metros: "))
    comprimento = float(input("Digite o comprimento em metros: "))
    area = (largura*comprimento)
    soma = soma + area
    resposta = (input("Deseja informar outro cômodo? (SIM/NÃO) "))
print(f"A área total da sua residência é: {soma} metros")
