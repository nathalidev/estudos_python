"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args) # é uma função que recebe outra função com uma tupla que empacota todos os seus argumentos dentro do args


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)