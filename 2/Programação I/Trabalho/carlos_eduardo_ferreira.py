voto_em_branco = 0
voto_samuca = 0
voto_neto = 0
voto_baltazar = 0
voto_nulo = 0
eleitores = 0

while True:
    voto = int(input('Escolha seu voto:\n0 - Branco\n1 - Samuca\n2 - Neto\n3 - Baltazar\n>=4 - Nulo\n  '))
    if voto == -1:
        break
    elif voto == 0:
        voto_em_branco = voto_em_branco + 1
    elif voto == 1:
        voto_samuca = voto_samuca + 1
    elif voto == 2:
        voto_neto = voto_neto + 1
    elif voto == 3:
        voto_baltazar = voto_baltazar + 1
    elif voto >= 4:
        voto_nulo = voto_nulo + 1
    eleitores = eleitores + 1
        
if (voto_samuca) == (voto_neto) and (voto_samuca) == (voto_baltazar):
    print(f'A votação ficou empatada com {voto_samuca} votos para cada candidato!\n')
elif (voto_samuca) == (voto_neto) and (voto_samuca) > (voto_baltazar):
    voto = int(input('Segundo turno!\nDigite 1 para escolher o candidato Samuca ou 2 para o candidato Neto\n'))
    if voto == 1:
        print(f'O candidato número 1 - Samuca foi o vencedor com {voto_samuca} no primeiro turno e ganhou no desempate com o candidato Neto!')
    else:
        print(f'O candidato número 2 - Neto foi o vencedor com {voto_neto} votos no primeiro turno e ganhou no desempate com o candidato Samuca!')
elif (voto_samuca) == (voto_baltazar) and  (voto_samuca) > (voto_neto):
    voto = int(input('Segundo turno!\nDigite 1 para escolher o candidato Samuca ou 2 para o candidato Baltazar\n'))
    if voto == 1:
        print(f'O candidato número 1 - Samuca foi o vencedor com {voto_samuca} no primeiro turno e ganhou no desempate com o candidato Baltazar!')
    else:
        print(f'O candidato número 3 - Baltazar foi o vencedor com {voto_baltazar} votos no primeiro turno e ganhou no desempate com o candidato Samuca!')
elif (voto_neto) == (voto_baltazar) and (voto_neto) > (voto_samuca):
    voto = int(input('Segundo turno!\nDigite 1 para escolher o candidato Neto ou 2 para o candidato Baltazar\n'))
    if voto == 1:
        print(f'O candidato número 2 - Neto foi o vencedor com {voto_neto} votos no primeiro turno e ganhou no desempate com o candidato Baltazar! ')
    else:
        print(f'O candidato número 3 - Baltazar foi o vencedor com {voto_baltazar} votos no primeiro turno e ganhou no desempate com o candidato Neto!')
elif (voto_samuca) > (voto_neto) and (voto_samuca) > (voto_baltazar):
    print(f'O candidato número 1 - Samuca foi o vencedor com {voto_samuca} votos!')
elif (voto_neto) > (voto_samuca) and (voto_neto) > (voto_baltazar):
    print(f'O candidato número 2 - Neto foi o vencedor com {voto_neto} votos!')
elif (voto_baltazar) > (voto_neto) and (voto_baltazar) > (voto_samuca):
    print(f'O candidato número 3 - Baltazar foi o vencedor com {voto_baltazar} votos!')
print(f'A quantidade de votos em branco foi: {voto_em_branco}!\nA quantidade de votos nulos foi: {voto_nulo}!\nA quantidade de eleitores foi: {eleitores}!')
