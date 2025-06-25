"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for indice, nome in enumerate(lista):
    print(indice, nome, type(lista[indice]))