# Exercício Hardcore de Lógica:
# Objetivo: implementar manualmente uma função que receba uma lista de números inteiros,
#           remova os elementos duplicados e ordene os valores em ordem crescente,
#           retornando uma nova lista como resultado.
#
# Regras:
# - Não usar funções prontas como set(), sorted(), len(), min(), max(), append(), remove(), pop(), insert().
# - Todo o controle deve ser feito manualmente com loops, comparações e manipulação direta de índices.
# - O algoritmo deve funcionar para listas de qualquer tamanho.
#
# Exemplo:
# Entrada: [5, 2, 9, 1, 5, 6, 2]
# Saída:   [1, 2, 5, 6, 9]

def retirar_repetidos(lista):
    inicio_lista_a_comparar = 1
    indice_lista_repetidos = 0
    lista_repetidos = [0]
    delimitador_lista_repetidos = 1
    contador_passagem = 0
    for termo in lista:
        if termo in lista_repetidos:
            continue
        else:
            for termo_comparacao in lista[inicio_lista_a_comparar::]:
                inicio_lista_a_comparar +=1
                if termo == termo_comparacao:
                    lista_repetidos = lista_repetidos * delimitador_lista_repetidos
                    delimitador_lista_repetidos +=1
                    lista_repetidos[indice_lista_repetidos] = termo
                    indice_lista_repetidos +=1
            
    return lista_repetidos

print(retirar_repetidos([5, 2, 9, 1, 5, 6, 2]))