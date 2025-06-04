"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None #boa pratica sempre definir variaveis que serão usadas em if e else fora dessas estruturas

if condicao:
    passou_no_if = True # a flag aqui seria a passou_no_if que serve para indicar a condição de que o código passou pelo if e para isso que as flags servem

    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
    
print(f"endereço interno na memória da variavel 'passou_no_if' {id(passou_no_if)}") 
# Mesmo que uma variável tenha o valor None, ela ainda ocupa um lugar na memória
# a função id() endereço interno na memória onde o objeto está armazenado (enquanto ele existir).