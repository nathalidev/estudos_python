# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
""" se o preço daquele produto for maior que 20 desempacoto aquele produto multiplicando o preço dele por 1,05 se não eu só desempacoto o produto em si e crio a lista é isso? """

print(novos_produtos)
for produto in novos_produtos:
    print(" | ".join(f"{chave}:{valor}" for chave , valor in produto.items()))
# print(*novos_produtos, sep='\n')

#e se eu quisesse desempacotar os dicionários dentro de produtos?
