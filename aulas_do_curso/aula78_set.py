# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# ------------------------------------------------------

# 🔹 add(elem)
# Adiciona um único elemento ao set.
# s = {1, 2}
# s.add(3)
# print(s)  # {1, 2, 3}
# Se o valor já existir, ele ignora — sem duplicar, sem erro.

# ------------------------------------------------------

# 🔹 update(iterável)
# Adiciona vários elementos de uma vez. Aceita listas, tuplas, outros sets, etc.

# ------------------------------------------------------

# s = {1, 2}
# s.update([3, 4], (5, 6), {7})
# print(s)  # {1, 2, 3, 4, 5, 6, 7}
# É como se fizesse vários add() seguidos.

# ------------------------------------------------------

# 🔹 clear()
# Zera o set. Apaga tudo.
# s = {1, 2, 3}
# s.clear()
# print(s)  # set()

# ------------------------------------------------------

# 🔹 discard(elem)
# Remove o elemento se existir. Se não existir, ignora (não dá erro).
# s = {1, 2, 3}
# s.discard(2)   # remove
# s.discard(99)  # não faz nada

# ------------------------------------------------------

# 🚀 Dica ninja:
# Quer tentar remover sem quebrar tudo? Usa discard.
# Quer remover e garantir que o valor está lá mesmo? Usa remove (mas ele explode se o item não existir).

# ------------------------------------------------------

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados
s1.discard('Olá mundo') # discard diferente do remove não da erro caso não exista o valor em questão no set
s1.discard('Luiz')
# print(s1)

s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)