from itertools import combinations, permutations, product

# Dados de teste: uma lista com 3 elementos
elementos = ['A', 'B', 'C']
tamanho = 2

print(f"--- Dados Iniciais: {elementos} (Tamanho do grupo: {tamanho}) ---\n")

# 1. COMBINATIONS (Combinações)
# A ordem NÃO importa. Se [A, B] já existe, [B, A] é descartado. 
# Não repete o mesmo elemento com ele mesmo.
comb = list(combinations(elementos, tamanho))
print(f"1. Combinations (Total: {len(comb)}):")
print(comb)
print("👉 Note que 'A' combina com 'B', mas 'B' com 'A' não aparece porque a ordem não importa.\n")


# 2. PERMUTATIONS (Permutações)
# A ordem IMPORTA. [A, B] e [B, A] são considerados resultados diferentes.
# Não repete o mesmo elemento com ele mesmo.
perm = list(permutations(elementos, tamanho))
print(f"2. Permutations (Total: {len(perm)}):")
print(perm)
print("👉 Note que agora temos tanto ('A', 'B') quanto ('B', 'A') porque a ordem importa.\n")


# 3. PRODUCT (Produto Cartesiano)
# A ordem IMPORTA e PERMITE REPETIÇÃO (combina o elemento com ele mesmo).
# Equivale a usar loops aninhados (for dentro de for).
# repeat é sempre um argumento nomeado.
prod = list(product(elementos, repeat=tamanho)) 
print(f"3. Product (Total: {len(prod)}):")
print(prod)
print("👉 Note que além da ordem importar, temos elementos repetidos como ('A', 'A'), ('B', 'B') e ('C', 'C').\n")
