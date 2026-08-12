"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
A ordem do número duplicado é considerada a partir da segunda
ocorrência do número, ou seja, o número duplicado em si.
Exemplo:
[1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
[1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
[1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def repetidos(listas):
    """
    Para cada lista:

    - Procura números que aparecem mais de uma vez.
    - Para cada número repetido, encontra onde ele aparece pela 2ª vez.
    - Guarda a posição dessa 2ª ocorrência.
    - A menor posição é a primeira duplicação da lista.
    - Usa essa posição para descobrir qual é o número duplicado.
    - Se nenhum número se repetir, não há duplicado.

    Exemplo:
        [1, 2, 3, 4, 3, 2, 1]

        3 → 2ª ocorrência no índice 4
        2 → 2ª ocorrência no índice 5
        1 → 2ª ocorrência no índice 6

        Menor índice = 4
        lista[4] = 3

        Resultado: 3

    Importante:
        Não importa qual número é o primeiro a ser descoberto como
        repetido. O que importa é qual SEGUNDA ocorrência aparece
        primeiro na lista.
    """
    for lista in listas:
        tem_repetido = False
        lista_indices = []

        for numero in lista:
            if lista.count(numero) > 1:
                tem_repetido = True
                indice_do_numero = lista.index(numero)
                indice_do_numero2 = lista.index(numero, indice_do_numero+1)
                lista_indices.append(indice_do_numero2)
        if tem_repetido:
            indice_do_numero = min(lista_indices)
            numero_repetido = lista[indice_do_numero]
            print(f"Tem repetido é o {numero_repetido}")
        else:
            print("Não tem repetido")

repetidos(lista_de_listas_de_inteiros)

# o primeiro duplicado é decidido pela segunda ocorrencia
# e não se ele literalmente é o primeiro repetido certo