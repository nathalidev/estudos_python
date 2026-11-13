"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 #variavel global
# Alternativas melhores para definir o valor da variavel global:
# Passar a variável como argumento pra função.

# Retornar o novo valor da função e atribuir fora.

def escopo():
    global x #referencio a variavel global
    x = 10 #atribuo a variavel global o valor 10

    def outra_funcao():
        global x #nonlocal x  pega o x da função pai

        x = 11 #agora x vale 11
        y = 2 #y é 2 existindo só nesse escopo
        print(x, y)

    outra_funcao() # ao chama escopo() ela executa outra_funcao()
    print(x)


print(x) #imprimo 1
escopo() # beleza agora x vale 11 e tem o y =2, eu imprimo 11, 2 depois só o x queria seria 11
print(x) # imprimo o x que agora vale 11
# ou seja
# 1
# 11, 2
# 11
# 11