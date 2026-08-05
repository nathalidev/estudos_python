def multiplicadora (*args):
    valor_inicial = 1
    for arg in args:
        valor_inicial *= arg
    return valor_inicial

print(multiplicadora(8, 94, 3, 6, 7))