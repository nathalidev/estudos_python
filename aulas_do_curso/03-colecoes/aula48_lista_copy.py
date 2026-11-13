"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # com o copy lista_b recebe o valor daquele momento de lista a se lista a for modificada depois não influencia na b agora se eu atribuir "=" a lista b muda junto

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)