"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas

🧠 Tipagem dinâmica
Você não precisa declarar o tipo da variável. O Python descobre sozinho.

🔒 Tipagem forte
print(5 + "5")  # Erro! Não dá pra somar int com str
Python não converte tipos diferentes automaticamente em operações.
"""
print(1234)

# Aspas simples
print('Luiz Otávio')
print(1, 'Luiz "Otávio"') # se eu quero imprimir aspas é só fazer a diferenciação delas dentro do print

print("-" * 10)

# Aspas duplas
print("Luiz Otávio")
print(2, "Luiz 'Otávio'") # vice-versa seguindo a mesma regra que falei no comentário acima 

print("-" * 10)

# Escape
print("Luiz \"Otávio\"") #o que eu coloco apos o escape (\) será printado

print("-" * 10)

# r
print(r"Luiz \"Otávio\"") #caso eu queira imprimir até o caractere de espaço