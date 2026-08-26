def nao_sei(lista)-> list:
    contador = 1
    contador_repetidos = 0
    contador_tamanho = 0
    troca_termo1 = False
    if troca_termo1 == False:
        for termo1 in lista:
            contador_tamanho +=1
            for termo2 in lista[contador::]:
                if termo1 > termo2:
                    lista[contador] = termo1
                    lista[(contador-1)] = termo2
                    contador+=1
                elif termo1 == termo2:
                    contador_repetidos +=1
                    lista[-1] = termo2
                    contador+=1
                    continue
                else:
                    lista[contador] = termo2
                    lista[(contador-1)] = termo1
                    troca_termo1 = True
    else:
        troca_termo1 = False
        for termo1 in lista[contador::]:
            for termo2 in lista[contador::]:
                if termo1 > termo2:
                    lista[contador] = termo1
                    lista[(contador-1)] = termo2
                    contador+=1
                elif termo1 == termo2:
                    contador_repetidos +=1
                    lista[-1] = termo2
                    contador+=1
                    continue
                else:
                    lista[contador] = termo2
                    lista[(contador-1)] = termo1
                    troca_termo1 = True
    tamanho_final = contador_tamanho-contador_repetidos
    return lista[:tamanho_final:]

print(nao_sei([5, 2, 9, 1, 5, 6, 2]))