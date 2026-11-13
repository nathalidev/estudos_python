def multiplicando (*args):
    acumulador = 1
    for arg in args:
        if type(arg) != int:
            return "A função só funciona com números!" #return encerra a função na hora
        else:
            acumulador *= arg
    return acumulador

print(multiplicando(1,"a",3))

# def par_ou_impar (n):
#     if type(n) != int:
#         print("A função só funciona com números!")
#     else:
#         par_impar = f"{n} é ímpar" if n%2>0 else f"{n} é par"
#         return par_impar

# print (par_ou_impar("a")) não dar print dentro de função.