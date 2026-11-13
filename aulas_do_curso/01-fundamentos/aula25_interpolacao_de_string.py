"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500)) #08 adiciona zeros até ter 8 casas. 
# print(f'O hexadecimal de {1500} é {1500:08X}') Exemplo equivalente de formatação porém utilizando a f-string.
#evitar esse estilo de formatar strings, utilizar o f-string