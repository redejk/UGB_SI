def votacao():
    votos = []
    voto_em_branco = 0
    voto_samuca = 0
    voto_neto = 0
    voto_baltazar = 0
    voto_nulo = 0
    print('*****  Simulação de uma eleição para prefeito na cidade de Volta Redonda - RJ  *****\n')
    while True:
        voto = int(input('Escolha seu voto:\n0 = Voto em Branco\n1 = Candidato Samuca\n2 = Candidato Neto\n3 = Candidato Baltazar\n4 ou maior = Voto Nulo\nDigite -1 para encerrar a votação.\n\n'))
        if voto == -1:
            break
        else:
            votos.append(voto)

    eleitores = len(votos)

    for voto in votos:
        if voto == 0:
            voto_em_branco = voto_em_branco +1
        elif voto == 1:
            voto_samuca = voto_samuca +1
        elif voto == 2:
            voto_neto = voto_neto +1
        elif voto == 3:
            voto_baltazar = voto_baltazar +1
        else:
            voto_nulo = voto_nulo +1
            
    if (voto_samuca) == (voto_neto) and (voto_samuca) == (voto_baltazar):
        resultado = (f'A votação ficou empatada com {voto_samuca} voto(s) para cada candidato!\n')
    elif (voto_samuca) == (voto_neto) and (voto_samuca) > (voto_baltazar):
        voto = int(input('Segundo turno!\nDigite 1 para escolher o candidato Samuca ou 2 para o candidato Neto\n'))
        if voto == 1:
            resultado = (f'O candidato número 1 - Samuca foi o vencedor com {voto_samuca} voto(s) no primeiro turno e ganhou no desempate com o candidato Neto!')
        else:
            resultado = (f'O candidato número 2 - Neto foi o vencedor com {voto_neto} voto(s) no primeiro turno e ganhou no desempate com o candidato Samuca!')
    elif (voto_samuca) == (voto_baltazar) and  (voto_samuca) > (voto_neto):
        voto = int(input('Segundo turno!\nDigite 1 para escolher o candidato Samuca ou 2 para o candidato Baltazar\n'))
        if voto == 1:
            resultado = (f'O candidato número 1 - Samuca foi o vencedor com {voto_samuca} voto(s) no primeiro turno e ganhou no desempate com o candidato Baltazar!')
        else:
            resultado = (f'O candidato número 3 - Baltazar foi o vencedor com {voto_baltazar} voto(s) no primeiro turno e ganhou no desempate com o candidato Samuca!')
    elif (voto_neto) == (voto_baltazar) and (voto_neto) > (voto_samuca):
        voto = int(input('Segundo turno!\nDigite 1 para escolher o candidato Neto ou 2 para o candidato Baltazar\n'))
        if voto == 1:
            resultado = (f'O candidato número 2 - Neto foi o vencedor com {voto_neto} voto(s) no primeiro turno e ganhou no desempate com o candidato Baltazar! ')
        else:
            resultado = (f'O candidato número 3 - Baltazar foi o vencedor com {voto_baltazar} voto(s) no primeiro turno e ganhou no desempate com o candidato Neto!')
    elif (voto_samuca) > (voto_neto) and (voto_samuca) > (voto_baltazar):
        resultado = (f'O candidato número 1 - Samuca foi o vencedor com {voto_samuca} voto(s)!')
    elif (voto_neto) > (voto_samuca) and (voto_neto) > (voto_baltazar):
        resultado = (f'O candidato número 2 - Neto foi o vencedor com {voto_neto} voto(s)!')
    elif (voto_baltazar) > (voto_neto) and (voto_baltazar) > (voto_samuca):
        resultado = (f'O candidato número 3 - Baltazar foi o vencedor com {voto_baltazar} voto(s)!')
    conclusao = (f'A quantidade de voto(s) em branco foi: {voto_em_branco}!\nA quantidade de voto(s) nulo foi: {voto_nulo}!\nA quantidade de eleitores foi: {eleitores}!')
    return (f"{resultado}\n{conclusao}")
eleicao = votacao()
print(eleicao)