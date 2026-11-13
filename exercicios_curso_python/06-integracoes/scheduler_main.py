import schedule
import time
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # pela pasta projeto_teste_importacoes estar no mesmo nivel da pasta atual é necessário adicionar o caminho dela no sys.path
from schedule_1 import primeira_tarefa_agendada
from projeto_teste_importacoes.scheduler_2 import segunda_tarefa_agendada

primeira_tarefa_agendada()
segunda_tarefa_agendada()

# schedule.every().second.do(primeira_tarefa_agendada) # a todo segundo faça a tarefal tal
primeira_tarefa_agendada() # executa a tarefa uma vez antes de entrar no loop
# from schedule import repeat
# from schedule import every

# @repeat(every().second)
# def primeira_tarefa_agendada():
#     print("Executando tarefa agendada...")
# poderia fazer assim também o resultado final seria igual

# posso usar o repeat como decorator ou usar o .do() para agendar a tarefa juntamente com o every()

schedule.every(10).seconds.do(segunda_tarefa_agendada) # a cada 10 segundos faça a tarefa tal

# Agendar para rodar todos os dias às 10:30
# schedule.every().day.at("10:30").do(tarefa_diaria)
# O método .day.at() permite definir um horário exato para rodar uma função diariamente.
# poderia especificar um dia da semana também
# schedule.every().hour.at(":17").do(tarefa_diaria) - fazendo isso a tarefa vai acontecer a cada hora no minuto 17

# ele vai rodar sempre seguindo o fuso do sistema na qual ele está rodando poderia ser um servidor porem no meu caso é meu pc local

# schedule.every().day.at("HH:MM").until("HH:MM")
# Esse método é útil quando você quer que uma tarefa só seja executada dentro de um intervalo de tempo específico.

# Executa a tarefa todos os dias às 10:00, mas só até 18:00
# schedule.every().day.at("10:00").until("18:00").do(tarefa)

while True:
    schedule.run_pending() # roda as tarefas que estão agendadas
    time.sleep(1) # espera 1 segundo para rodar novamente o loop se não iria travar a CPU


# as opções do schedule.every() definem com que frequência uma tarefa vai rodar.
# Aqui vai o cardápio completo 👇

# 🕒 Frequências básicas
# import schedule

# schedule.every().second          # a cada 1 segundo
# schedule.every().minute          # a cada 1 minuto
# schedule.every().hour            # a cada 1 hora
# schedule.every().day             # uma vez por dia
# schedule.every().week            # uma vez por semana

# 🔢 Frequências com intervalo
# schedule.every(10).seconds       # a cada 10 segundos
# schedule.every(5).minutes        # a cada 5 minutos
# schedule.every(2).hours          # a cada 2 horas
# schedule.every(3).days           # a cada 3 dias
# schedule.every(2).weeks          # a cada 2 semanas

# 📅 Especificar dia da semana
# schedule.every().monday          # toda segunda e por ai vai 
# schedule.every().tuesday
# schedule.every().wednesday
# schedule.every().thursday
# schedule.every().friday
# schedule.every().saturday
# schedule.every().sunday