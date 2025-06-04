'''
🔢 Verificar se uma matriz 3x3 é um quadrado mágico
Ou seja:

Ler 9 números (3 por linha, total de 3 linhas).

Montar uma matriz 3x3 com esses números.

Verificar se:

As 3 linhas têm a mesma soma.

As 3 colunas têm a mesma soma.

As 2 diagonais têm a mesma soma.

Se tudo for igual, printa: "Quadrado Mágico!"

Se alguma soma for diferente, printa: "Azedou irmão"
'''

matriz = [] #cria a matriz 

for i in range(3):
    numeros_do_quadrado = input("Digite três n° para o quadrado: ").split(" ") #crio 3 listas com numeros
    lista_convertida = [] 
    # a lista acima sera string e para fazer as operações precisam ser n° essa lista armazena os convertidos
    
    for n in numeros_do_quadrado: #nao posso converter uma lista tem que ser termo a termo
        lista_convertida.append(int(n)) #adiciono os convertidos a lista nova
    matriz.append(lista_convertida) #a matriz pega as 3 listas convertida
    
soma_primeira_linha = sum(matriz[0]) # faço todas as soma possiveis para ver se batem e da o quadrado maigco
soma_segunda_linha = sum(matriz[1])
soma_vertical_esquerda = matriz[0][0] + matriz[1][0] + matriz[2][0]
soma_ultima_linha = sum(matriz[2])
soma_vertical_direita = matriz[0][2] + matriz[1][2] + matriz[2][2]
soma_diagonal_esquerda = matriz[0][0] + matriz[1][1] + matriz[2][2]
soma_diagonal_direita = matriz[0][2] + matriz[1][1] + matriz[2][0]

if (
    soma_primeira_linha == soma_vertical_esquerda and
    soma_vertical_esquerda == soma_ultima_linha and
    soma_ultima_linha == soma_vertical_direita and
    soma_vertical_direita == soma_diagonal_esquerda and
    soma_diagonal_esquerda == soma_diagonal_direita and
    soma_diagonal_direita == soma_segunda_linha # se todas as linhas forem iguais da bom
):
    print("Quadrado Mágico!")
else:
    print("Azedou irmão")
