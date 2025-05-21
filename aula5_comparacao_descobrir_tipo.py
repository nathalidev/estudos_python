# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# Expressões com dois sinais de igual (==), conferem se um valor é igual a outro valor e se eles são do mesmo tipo.

# 🧠 Quer comparar 10 com "10" ignorando tipo?
# Você precisa converter um dos dois antes de comparar:

# int("10") == 10   # True
# str(10) == "10"   # True