"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a    = [1, 2, 3, 4, 5, 6, 7]
lista_b    = [1, 2, 3, 4]

================ resultado
lista_soma = [2, 4, 6, 8]
"""
import re

try:
    lista_1 = [int(x) for x in re.split(r"[-+, ]+", input("Insira 7 números inteiros:\n").strip())]
    lista_2 = [int(x) for x in re.split(r"[-+, ]+",input("Insira 4 números inteiros para fazer parte da 1° lista:\n").strip())]

except TypeError:
    print("Erro de tipo: você precisa digitar números inteiros!")

if len(lista_1) < 7 or len(lista_1) > 7:
    print("Vamos lá me dê 7 números cara...")

if len(lista_2) < 4 or len(lista_2) > 4:
    print("São 4 números amigo...")

lista_somada = [a + b for a, b in zip(lista_1, lista_2)]

print(f"Lista Final: {lista_somada}")

