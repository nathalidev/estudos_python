# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3) #-> fabrica_de_funcoes(soma) -> vai printar Decoradora 1 -> aninhada
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores() #decoradora = fabrica_de_funcoes
multiplica = decoradora(lambda x, y: x * y) # multiplica = fabrica_de_funcoes(lambda x, y: x * y) vai print decoradora 1

dez_mais_cinco = soma(10, 5) #fabrica_de_decoradores(1, 2, 3) retorna fabrica_de_funcoes; o @ então faz fabrica_de_funcoes(soma), que recebe a função soma e retorna aninhada; por isso soma passa a apontar para aninhada. Somente quando eu faço soma(10, 5) é que 10 e 5 entram em aninhada através de args.
dez_vezes_cinco = multiplica(10, 5) #aninhada(10,5) func é a lambda ou seja res = 50
print(dez_mais_cinco)
print(dez_vezes_cinco)