"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')

# POSSO MISTURAR ARGUMENTO POSICIONAL COM OS NOMEADOS?


# O ChatGPT disse:
# Pode sim, mas tem regra:
# 👉 Argumentos posicionais sempre vêm antes dos nomeados.

# ✅ Exemplo válido:

# def exemplo(a, b, c):
#     print(a, b, c)

# exemplo(1, b=2, c=3)  # OK ao nomear um argumento voce tem que nomear todos os outros que vem depois
# ---------------------------------------------
# ❌ Exemplo inválido:
# exemplo(a=1, 2, 3)  # ERRO: não pode nomeado antes de posicional

# quando devo deixar um "return" explicito ali ou não?
# RESPOSTA: Se você vai usar o resultado depois, use return.
# Se não vai usar pra nada além da execução ali na hora, pode só fazer e pronto.

