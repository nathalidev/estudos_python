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

def tamanho_lista(lista):
    contador = 0
    for termo in lista:
        contador+=1
    return contador

def retirar_repetidos(lista, tamanho_total):
    inicio_lista_a_comparar = 1
    indice_lista_repetidos = 0
    lista_repetidos = [0]
    delimitador_lista_repetidos = 0
    contador_comparacao = 0
    for termo in lista:
        if termo in lista_repetidos:
            continue
        else:
            for termo_comparacao in lista[inicio_lista_a_comparar::]:
                contador_comparacao += 1
                if termo == termo_comparacao:
                    delimitador_lista_repetidos +=1
                    lista_repetidos = lista_repetidos * delimitador_lista_repetidos
                    lista_repetidos[indice_lista_repetidos] = termo
                    indice_lista_repetidos +=1
                elif termo_comparacao == lista[-1] and (contador_comparacao == (tamanho_total-1)):
                    inicio_lista_a_comparar +=1
                    contador_comparacao = 0
                    break
                else:
                    continue
                    # essa variavel precisa ser acrescida toda vez que vamos passar por um termo 
            
    return lista_repetidos

tamanho = tamanho_lista([5, 2, 9, 1, 5, 6, 2])
print(retirar_repetidos([5, 2, 9, 1, 5, 6, 2], tamanho))