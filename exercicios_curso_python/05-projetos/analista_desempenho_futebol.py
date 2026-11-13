def aplicar_metricas(funcao, *args):
    return funcao(*args)

def avaliador_de_jogador(nome_do_jogador):
    def funcao_interna(*args):
        gols, assistencias, passes, posicao = args
        jogador = {}

        jogador['Nome'] = nome_do_jogador

        jogador['Posição'] = posicao

        jogador['Total de Gols'] = gols

        jogador['Total de Assistências'] = assistencias

        jogador['Passes certos'] = passes

        if posicao == 'Atacante':
            jogador['Indice de desempenho'] = (jogador['Total de Gols'] * 5 + jogador['Total de Assistências'] * 3 + jogador['Passes certos'] * 0.05)

        elif posicao == 'Meio-campista':
            jogador['Indice de desempenho'] = (jogador['Total de Gols'] * 3 + jogador['Total de Assistências'] * 4 + jogador['Passes certos'] * 0.2)

        else: 
            jogador['Indice de desempenho'] = (jogador['Total de Gols'] * 2 + jogador['Total de Assistências'] * 2 + jogador['Passes certos'] * 0.3)

        avaliacao_indice = 'Excelente' if jogador['Indice de desempenho'] >= 101 else 'Muito bom' if jogador['Indice de desempenho'] >= 71 else 'Bom' if jogador['Indice de desempenho'] >= 41 else 'Regular' if jogador['Indice de desempenho'] >= 21 else 'Fraco'

        return f'{jogador}/nAvaliação Geral: {avaliacao_indice}'
    return funcao_interna

nome_do_jogador = input("Digite o nome do jogador a ser avaliado: ")
posicao = input("Digite a posição do jogador (Atacante, Meio-campista, Defensor): ")
gols = int(input("Digite o número de gols marcados: "))
assistencias = int(input("Digite o número de assistências feitas: "))
passes = int(input("Digite o número de passes certos: "))
avaliar = avaliador_de_jogador(nome_do_jogador)
resultado = aplicar_metricas(avaliar, gols, assistencias, passes, posicao)
print(resultado)

