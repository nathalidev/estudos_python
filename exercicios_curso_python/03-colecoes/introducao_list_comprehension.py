lista_cubos = [x**3 for x in range(10)]
print(lista_cubos)

lista_maiusculas = [x.capitalize() for x in ["oi", "alô", "tchau"]]
print(lista_maiusculas)

matriz = [[1, 2], [3, 4], [5]]

# recriando a matriz, mas só com elementos maiores que 2
nova_matriz = [[x for x in linha if x > 2] for linha in matriz]

print(nova_matriz)
# Saída: [[], [3, 4], [5]]
