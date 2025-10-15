tarefas = [
    "Estudar para a prova",
    "Fazer compras",
    "Responder e-mails",
    "Limpar a casa",
    "Ir à academia",
    "Ligar para a avó",
    "Organizar documentos",
    "Planejar a semana"
]

def adicionar_tarefa(tarefa):
    tarefas.append(str(tarefa))

def remover_tarefa(tarefa):
    if not str(tarefa) in tarefas:
        print("Essa tarefa não existe na lista!")