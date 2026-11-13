# Nível 2 – Funções e estruturas

# Funções

# Crie uma função que recebe dois números e retorna o maior.

# Crie uma função que calcula a média de uma lista de números.

# Dicionários

# Crie um dicionário para armazenar nome e idade de 3 pessoas.

# Imprima o nome da pessoa mais velha.

# Loops avançados

# Percorra a lista [2, 4, 6, 8, 10] e imprima o dobro de cada número.

# def maior_numero(numeros):
#     return max(numeros)
numeros = []
for i in range(2):   
    numero = int(input("Digite um n°: "))
    numeros.append(numero)
# print(maior_numero(numeros))

maior_numero = lambda numeros : numeros[0] if numeros[0] > numeros[1] else numeros[1]
print(maior_numero(numeros))

media = lambda numeros : int(sum(numeros))/2
print(media(numeros))

# -------------------------------------------------------------------
dicionario = {}

for i in range(3):
    dicionario['Nome'] = input("Qual seu nome: ")
    dicionario['Idade'] = input("Qual sua idade: ")

print(dicionario)
