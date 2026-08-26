# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(cidades: list , siglas: list):
    lista_final = []
    for x, y in zip(cidades, siglas):
        cidade_estado = (x, y)
        lista_final.append(cidade_estado)
    print(lista_final)

zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'], ['BA', 'SP', 'MG', 'RJ'])

# zip() pega elementos de várias sequências (listas, tuplas, etc.) e os agrupa em tuplas.
# Ele para no menor iterável, evitando erros de índice.