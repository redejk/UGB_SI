'''
Ler 2 notas de um aluno UGB e mostrar se o aluno foi aprovado / reprovado / com final
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = round(((nota1 + nota2) / 2),1)
if media >= 7.0:
    print("Parabens, voce foi aprovado!")
    print(f"Sua media foi: {media}")
elif media <=3.0:
    print("Voce foi reprovado, estude mais!")
    print(f"Sua media foi: {media}")
elif (media >=3.1) and (media <=6.9):
    print(f"Sua media foi: {media}")
    print("Voce precisa fazer uma prova final!")
    final = float(input("Digite a nota da prova final: "))
    mediafinal = round(((media + final) / 2),1)
    if mediafinal >= 5.0:
        print("Voce foi aprovado com final!")
        print(f"Sua media final foi: {mediafinal}")
    else:
        print("Voce ficou reprovado!")
        print(f"Sua media final foi: {mediafinal}")

'''
Mesmo exercicio, porem com uso de uma funcao
https://www.delftstack.com/pt/howto/python/python-truncate-float-python/
documentacao python trunc: https://docs.python.org/pt-br/3/library/math.html
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = ((nota1 + nota2) / 2)

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

media = truncate(media, 1)

if media >= 7.0:
    print("Parabens, voce foi aprovado!")
    print(f"Sua media foi: {media}")
elif media <=3.0:
    print("Voce foi reprovado, estude mais!")
    print(f"Sua media foi: {media}")
elif (media >=3.1) and (media <=6.9):
    print(f"Sua media foi: {media}")
    print("Voce precisa fazer uma prova final!")
    final = float(input("Digite a nota da prova final: "))
    mediafinal = ((media + final) / 2)
    mediafinal = truncate(mediafinal, 1)
    if mediafinal >= 5.0:
        print("Voce foi aprovado com final!")
        print(f"Sua media final foi: {mediafinal}")
    else:
        print("Voce ficou reprovado!")
        print(f"Sua media final foi: {mediafinal}")