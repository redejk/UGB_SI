agenda = {}
agenda['Nome'] = input("Digite o nome da pessoa: ")
agenda['Telefone'] = int(input("Digite o telefone da pessoa: "))
for k, v in agenda.items():
    print(f"{k} - {v}")
