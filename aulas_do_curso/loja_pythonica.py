import copy 
produtos = [
    {"nome": "Camisa", "preco": 50.0},
    {"nome": "Calça", "preco": 80.0},
    {"nome": "Tênis", "preco": 120.0},
    {"nome": "Boné", "preco": 25.0},
]

def aumentar_preco(produtos, porcentagem):
    produtos_recalculados = [
        {'nome': p["nome"], 'preco' : round(p["preco"] + p["preco"] * (porcentagem/100), 2)}
        for p in copy.deepcopy(produtos)
    ]

    return produtos_recalculados

print(aumentar_preco(produtos, 10))

def ordenar_produtos(produtos, chave, reverso=False):
    produtos_ordenados = sorted(copy.deepcopy(produtos), key= lambda produto : produto[chave])
    return produtos_ordenados

print(ordenar_produtos(produtos, "preco"))



