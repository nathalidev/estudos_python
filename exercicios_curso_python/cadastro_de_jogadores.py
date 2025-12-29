jogadores = []
while True:
    jogador = {}
    try:
        nome = input("Digite o nome do jogador: ")
        jogador['Nome'] = nome
    except ValueError:
        print("Nome inválido. Tente novamente.")
        continue
    try:
        idade = int(input("Digite a idade do jogador: "))
        jogador['Idade'] = idade
    except ValueError:
        print("Idade inválida. Tente novamente.")
        continue
    try:
        posicao = input("Digite a posição do jogador: ")
        jogador['Posição'] = posicao
    except ValueError:
        print("Posição inválida. Tente novamente.")
        continue

    while True:
        continuar = input("Deseja cadastrar outro jogador? (s/n): ")
        if continuar.lower() in ('s', 'sim'):
            break
        elif continuar.lower() in ('n', 'não', 'nao'):
            for chave, valor in jogador.items():
                print(f"{chave}: {valor}")
                print("\n")
            exit()
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
            pass


