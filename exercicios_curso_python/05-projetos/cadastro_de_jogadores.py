jogadores = []
while True:
    jogador = {}

    nome = input("Digite o nome do jogador: ")
    if not nome.replace(" ", "").isalpha():
        raise ValueError("Nome deve conter apenas letras e espaços.")

    else:
        jogador['Nome'] = nome

    try:
        idade = int(input("\nDigite a idade do jogador: "))
        jogador['Idade'] = idade

        if idade < 0 or idade > 100:
            print("Seu jogador tem uma idade inválida. Tente novamente.")
            continue
    except ValueError:
        print("Idade inválida. Tente novamente.")
        continue

    posicao = input("\nDigite a posição do jogador: ")
    if not posicao.isalpha():
        raise ValueError("Posição deve conter apenas letras.")
    else:
        jogador['Posição'] = posicao
    
    jogadores.append(jogador)

    while True:
        continuar = input("\nDeseja cadastrar outro jogador? (s/n): ")
        if continuar.lower() in ('s', 'sim'):
            break
        elif continuar.lower() in ('n', 'não', 'nao'):
            for i, jogador in enumerate(jogadores):
                print("\n")
                print(f"{i + 1} {jogador['Nome']}")
                print(f"Idade: {jogador['Idade']}")
                print(f"Posição: {jogador['Posição']}")
            exit()
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
            pass


