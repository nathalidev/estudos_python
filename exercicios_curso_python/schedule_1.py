from schedule import repeat
from schedule import every

@repeat(every().second)
def primeira_tarefa_agendada():
    print("Executando tarefa agendada...")