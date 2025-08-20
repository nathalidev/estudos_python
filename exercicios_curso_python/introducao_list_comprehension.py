lista_cubos = [x**3 for x in range(10)]
print(lista_cubos)

lista_maiusculas = [x.capitalize() for x in ["oi", "alô", "tchau"]]
print(lista_maiusculas)

lista_matrix = [x.remove()for x, y in [[1,2],[3,4],[5]] if x[y] > 2]
print(lista_matrix)