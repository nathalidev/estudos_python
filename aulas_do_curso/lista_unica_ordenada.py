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
    lista_repetidos = []
    for termo in lista:
        if termo in lista_repetidos:
            inicio_lista_a_comparar +=1
            continue
        else:
            for termo_comparacao in lista[inicio_lista_a_comparar::]:
                if termo == termo_comparacao:
                    lista_repetidos += [termo]
            inicio_lista_a_comparar +=1
    if lista_repetidos == []:
        return "Não há elementos repetidos na lista"
                    
            
    return lista_repetidos

print(retirar_repetidos([5, 5, 5, 5]))

#próximo passo integrar isso com uma função de remoção desses termos repetidos que eu ja descobri via a função acima, e depois integrar com uma função de ordenação manual.

#a função só retorna uma repetição com base na segunda aparição do termo, então se o termo aparecer uma segunda vez na lista passada como parametro ele irá aparecer uma vez na nova lista com repetidos.
