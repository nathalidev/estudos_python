import decimal

# numero_1 = decimal.Decimal('0.1')
# numero_2 = decimal.Decimal('0.7')
numero_1 = 0.1
numero_2 = 0.7
print(repr(numero_1))
print(repr(numero_2))
numero_3 = numero_1 + numero_2
print(repr(numero_3))

print("="*20)

numero_1 = "0.1"
numero_2 = "0.7"
numero_1 = decimal.Decimal(numero_1)
numero_2 = decimal.Decimal(numero_2)
print(repr(numero_1))
print(repr(numero_2))
numero_3 = numero_1 + numero_2
print(numero_3)
# print(numero_3)
# print(f'{numero_3:.2f}')
# print(round(numero_3, 2))

# o python é traiçoeiro para calculos com float então é sempre bom converter os n/ do calculo em string e importar o decimal como acima
# para ver realmente o que ta por debaixo dos panos usa o repr. e antes de qualquer calculo com float chame o decimal porque se não o python vai zzoar o resultado do calculo