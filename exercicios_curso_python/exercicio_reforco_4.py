# from unidecode import unidecode

# contagem = {}

# texto = "Python é legal"

# texto_puro = unidecode(texto.lower()) # primeiro eu separo as palavras e depois coloco tudo em minusculo

# texto_sem_espaco = texto_puro.replace(" ", "") # depois eu removo os espacos

# lista_final = list(texto_sem_espaco)

# for letra in lista_final:
#     contagem[letra] = contagem.get(letra, 0) + 1

# print("\nContagem de letras:\n")
# for chave,valor in contagem.items():
#     print(f"{chave} : {valor}\n")

# ----------------------------------------------------------------------------------------------

# loja1 = {"caneta": 10, "caderno": 5}
# loja2 = {"caderno": 7, "lapis": 15}

# for chave,valor in loja1.items():
#     if chave in loja2:
#         loja2[chave] += valor
#     else:
#         loja2.update({chave: valor})

# print(loja2)

# ----------------------------------------------------------------------------------------------

# numeros = [1,2,3,4,5,6]

# lista_pares = list(filter(lambda numero : numero % 2 == 0, numeros)) #aqui a minha função lambda vai ser o filtro pros elemento que vão compor minha lista
# print(lista_pares)

# ----------------------------------------------------------------------------------------------

import copy

alunos = {"Ana": 8, "Bruno": 6, "Carlos": 7}

alunos_copia = copy.deepcopy(alunos)

for chave in alunos_copia.keys():
    alunos_copia.update({chave: alunos_copia.get(chave, 0) + 1})
print(alunos_copia)
print(alunos)
