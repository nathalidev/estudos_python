"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome): # essa função seria o closure pq ela lembra o valor da variavel saudacao mesmo depois de executar a função criar_saudacao
        return f'{saudacao}, {nome}!'
    return saudar # retorna a função interna com o valor de 'saudacao' encapsulado


falar_bom_dia = criar_saudacao('Bom dia') #essa variavel vai armazenar a função com o argumento definido
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome)) # aqui executamos a função closure, que já guarda o valor de 'saudacao', passando o 'nome' como argumento.
    print(falar_boa_noite(nome))# o closure tbm sera executado porque ele faz parte da funcao criar_saudacao