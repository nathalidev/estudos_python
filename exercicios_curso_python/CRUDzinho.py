import json
import os
import sys

def carregar_json(nome_arquivo):
    if os.path.exists(nome_arquivo): # Verifica se o arquivo "tarefas.json" existe no diretório atual
        with open(nome_arquivo, "r", encoding="utf-8") as f: # Abre o arquivo "tarefas.json" no modo leitura ('r')
            arquivo_leitura = json.load(f)  # Lê o conteúdo JSON do arquivo e transforma em objeto Python (lista, dicionário, etc.)

    else:
        arquivo_leitura=[]

    return arquivo_leitura

def editar_json(nome_arquivo, arquivo_leitura):
    with open(nome_arquivo, "w", encoding="utf-8") as f: # Abre o arquivos "tarefas.json" no modo escrita ('w')
        json.dump(arquivo_leitura, f, indent=4, ensure_ascii=False) # lista_tarefas é a estrutura de dados que quero salvar no arquivo 
        # "f" é o arquivo aberto pronto para ter mais conteúdo gravado em si 

while True:
    escolha_usuario = int(input("\n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Marcar como concluída ou pendente\n4 - Remover tarefa\n5 - Sair\nSua opção: "))

    lista_tarefas = carregar_json("tarefas.json")
    try: 
        if escolha_usuario == 1:
            descricao = input("Digite a descrição da tarefa: ")
            concluida = input("\nEla já foi concluida? Digite 1-Sim ou 2-Não\n")

            if concluida.upper() in ["SIM", "S", "1"]:
                concluida = "Concluída"
            
            elif concluida.upper() in ["NAO", "N", "2"]:
                concluida = "Pendente"

            else:
                print("Resposta inválida")

            lista_tarefas.append(
                f"{descricao} [{concluida}]"
            )

            editar_json("tarefas.json", lista_tarefas)

        if escolha_usuario == 2:
            for id, tarefa in enumerate(lista_tarefas, start=1):
                print(f"\n{id} {tarefa}")

        if escolha_usuario == 3: 
            for id, tarefa in enumerate(lista_tarefas, start=1):
                print(f"\n{id} {tarefa}")

            selecao_tarefa = int(input("\nInforme o id da tarefa a ter sua conclusão alterada: "))
            valor_selecionado  = lista_tarefas[selecao_tarefa-1]
            if "Concluída" in valor_selecionado:
                lista_tarefas[selecao_tarefa-1]=lista_tarefas[selecao_tarefa-1].replace("Concluída", "Pendente")
            else:
                lista_tarefas[selecao_tarefa-1]=lista_tarefas[selecao_tarefa-1].replace("Pendente", "Concluída") 

            editar_json("tarefas.json", lista_tarefas)

            for tarefa in lista_tarefas:
                print(f"\n{tarefa}")

        if escolha_usuario == 4:
            for tarefa in lista_tarefas:
                print(tarefa)
            selecao_tarefa = int(input("\nInforme o id da tarefa a ser excluida: "))
            lista_tarefas.pop(selecao_tarefa-1)

            editar_json("tarefas.json", lista_tarefas)

        if escolha_usuario == 5:
            sys.exit()

    except Exception as e:
        print(f"ERRO: {e}")


"""
Um arquivo CRUD é simplesmente um arquivo (ou programa) que permite realizar operações básicas de um sistema de dados. CRUD é um acrônimo que vem de:

C → Create (Criar): adicionar novos registros ou informações.

R → Read (Ler): visualizar ou listar os registros existentes.

U → Update (Atualizar): alterar informações já cadastradas.

D → Delete (Excluir): remover registros.


Um CRUD é a base de qualquer sistema que manipula dados. Serve para:

Gerenciar usuários, produtos, pedidos, tarefas… qualquer coisa que precise de registro.

Servir como backend de apps, sites ou até scripts simples, porque toda informação precisa ser criada, consultada, alterada ou apagada em algum momento.

Testar conceitos de programação e persistência de dados (no seu caso, usando JSON).

Basicamente: se você consegue fazer um CRUD, você sabe criar o esqueleto de quase qualquer sistema que lida com dados.
"""