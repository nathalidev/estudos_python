# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

# combinations em python gera combinações unicas diferente do product que gera o produto cartesiano que gera todas as combinações possiveis

from itertools import combinations, permutations, product


# def print_iter(iterator):
#     print(*list(iterator), sep='\n')
#     print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
# print_iter(product(*camisetas))
iterador = combinations(pessoas, 2)
#print(iterador) combinations retorna o iterador
#print(list(iterador)) tranformando em lista ai sim voce consegue ver as combinações em forma de uma lista de tuplas

lista_combination = list(iterador)

print(lista_combination, sep ='\n') #aqui sep nao faz efeito porque nao tem um segundo argumento no print.

print(lista_combination, "aldjsljdfsljfslfj", sep ='\n')

# sep serve para escolher o separador entre argumentos de um print a questão é que uma lista em um print é um argumento só

# tentar usar um separador no print usando map é muito trabalhoso é 
# necessário o separador em uma variavel separada e a lista depois usa separador.join com o map convertendo os elementos para string junto com a lista em si se não, não é possivel.

# mais afinal o que são:
    
#     *args
#     args por convenção inclusive mais pode ser qualquer coisa, ela simplesmente vai pegar todos os argumentos e empacota-los em um tupla.
    
#     **kwargs
#     novamente kwargs por convenção empacota  qualquer n° de argumento nomeado nome="Nathã" e joga tudo num dicionário
    
#     * (um asterisco): Desempacota uma lista ou tupla em elementos individuais ou junta listas.
    
# 	Exemplo: lista = [1, 2, 3], chamar funcao(*lista) é o mesmo que funcao(1, 2, 3).

#     ** (dois asteriscos): Desempacota um dicionário em argumentos nomeados ou mescla dicionários.
    
# 	Exemplo: dados = {'a': 1, 'b': 2}, chamar funcao(**dados) é o mesmo que funcao(a=1, b=2).

# O uso de um asterisco único isolado (*) na assinatura de uma função serve para obrigar o uso de argumentos nomeados (keyword-only arguments) para todos os parâmetros que vierem depois dele.