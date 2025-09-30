import sys 
import time
lista_tarefas = []
while True:
    try:
        opcao = int(input("\nEscolha uma opção:\n"
    "* 1-Adicionar uma tarefa\n"
    "* 2-Listar todas as tarefas\n"
    "* 3-Remover uma tarefa pelo número\n"
    "* 4-Sair do programa\n"
    "Sua Opção: "))
        
        if opcao == 1:
            nova_tarefa = input("\nQual a nova tarefa:\n")
            lista_tarefas.append(nova_tarefa)

        elif opcao == 2:
            print("\nLista de tarefas:\n", *(f"- {t}" for t in lista_tarefas), sep="\n")

        elif opcao == 3:
            apagar = int(input("Selecione o n° da tarefa a ser apagada:\n"))

            del lista_tarefas[apagar-1]

        elif opcao == 4:
            print("Tchau")
            time.sleep(2)
            sys.exit()


    except Exception as e:
        print(f"Erro inesperado {e}")

