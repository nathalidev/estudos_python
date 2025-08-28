# # Gerando uma lista de pares de 0 a 20 usando list comprehension
# from pprint import pprint

# lista_pares = [(x,y,z) for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) ]
# pprint(lista_pares)

# string = 'Otávio Miranda'
# nova_string = [
#     string[indice:indice + 2]
#     for indice in range(0, len(string), 2)
# ]

# print(nova_string)

nomes = ["Rogério Ceni", "Ronaldinho", "Rodrigo Nestor", "Lugano", "Neymar", "Otamendi"]
nova_lista = [nome[:-1] + nome[-1].upper() for nome in nomes]
print(nova_lista)
