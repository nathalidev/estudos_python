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

    print("Lista com produtos 10% mais caro:")
    for produto in produtos_recalculados:
        print(f'{produto}')
    print('\n')

    

aumentar_preco(produtos, 10)

def ordenar_produtos(produtos, chave, reverso):
    produtos_ordenados = sorted(copy.deepcopy(produtos), key= lambda produto : produto[chave], reverse = reverso)
    print(f"Lista de produtos organizados por {chave}:")
    for produto in produtos_ordenados:
        print(f'{produto}')
    print('\n')



ordenar_produtos(produtos, "preco", True)

ordenar_produtos(produtos, "nome", False)





