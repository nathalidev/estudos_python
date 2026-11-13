from copy import deepcopy
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

for produto in produtos:
    produto['preco'] = produto['preco'] + (produto['preco'] * (10/100))
    produto['preco'] = round(produto['preco'], 2)
    print(produto)

copia_produtos = deepcopy(produtos)

produto = input("Digite o nome do novo produto: ")
preco = float(input("Digite o valor do novo produto: "))

copia_produtos.append({"nome": produto, "preco": preco})

print("\nProdutos ordenados por valor")
copia_produtos_2 = deepcopy(copia_produtos)
copia_ordenada = sorted(copia_produtos_2, key = lambda produto : produto['preco'])

for produto in copia_ordenada:
    print(produto)

print("\nProdutos ordenados por nome")
copia_ordenada_2 = sorted(copia_produtos_2, key = lambda produto : produto['nome'])

for produto in copia_ordenada_2:
    print(produto)


# fazendo dessa forma o valor da chave preco se tornou uma string formatada e o python trata ela
# o que pode ser prejudicial na hora de ordenar porque se tratando de strings 100 vem antes de 20 por exemplo
# então para manter o valor numérico pode ser feito o round que arredonda para manter duas casas decimais.
# produto['preco'] = round(produto['preco'], 2)
#

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)