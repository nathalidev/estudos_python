# 3️⃣ Simulação simples de fila de espera com prioridade
# Crie uma função que recebe uma lista de tuplas (nome, prioridade) e retorna a ordem de atendimento, onde prioridade maior é atendida primeiro. Se a prioridade for igual, mantém a ordem original.

fila = [
    ("Carlos", 1),
    ("Ana", 3),
    ("Beatriz", 2),
    ("Rogério", 3),
    ("Fernanda", 5),
    ("Lucas", 1),
    ("Marcos", 2),
    ("Tatiane", 5),
    ("João", 4)
]

def ordenacao_fila (pacientes):
    pacientes_ordenados = sorted(pacientes, key=lambda x: x[1], reverse=True)
    return pacientes_ordenados

print(ordenacao_fila(fila))
