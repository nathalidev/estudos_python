# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

pessoa.setdefault('idade', 0)
# print(pessoa['nome'])
print("N° de  chaves:", len(pessoa))
print("\n")
for chave in pessoa.keys():
    print("Chave:", chave)
    # keys, values e items são iteráveis; posso dar um print neles se transformar em list
    # ou tuple ou posso fazer como nessa linha

print("a",len(pessoa))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)