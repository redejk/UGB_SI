nvogais = []
pvogais = []
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input("Digite uma palavra: ")
if (len(palavra)) <= 5:
    for i in palavra:
        if i in vogais:
            pvogais.append(i)
    print(pvogais)
else:
    for i in palavra:
        if i not in vogais:
            nvogais.append(i)
    print(nvogais)