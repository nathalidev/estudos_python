from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Andre', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])

grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])

for chave, grupo in grupos:
    print(f"Alunos que tiraram nota {chave}:")
    for aluno in list(grupo):
        print(f"{aluno}\n")
    
    print(f"-"*50+"\n")