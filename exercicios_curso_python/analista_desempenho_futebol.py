def aplicar_metricas(funcao, *args):
    return funcao(*args)

def avaliador_de_jogador(nome_do_jogador):
    def funcao_interna(*args):
        gols, assistencias, passes = args
        jogador = {}

        jogador['Nome'] = nome_do_jogador


        jogador['Total de Gols'] = gols


        jogador['Total de Assistências'] = assistencias

        jogador['Passes certos'] = passes

        jogador['Indice de desempenho'] = (jogador['Total de Gols'] * 4 + jogador['Total de Assistências'] * 3 + jogador['Passes certos'] * 0.1)

        return jogador
    return funcao_interna

avaliar = avaliador_de_jogador("Nathã")
resultado = aplicar_metricas(avaliar, 3, 18, 450)
print(resultado)

