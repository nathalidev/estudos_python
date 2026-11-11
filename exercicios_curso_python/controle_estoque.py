from pynput import keyboard
import os
import signal
TECLA_INTERRUTORA = keyboard.Key.esc 

# eu envio um sinal de interrupção pro processo atual
# o sinal de interrupção é o signal.signit 
# o getpid pega o id do processo atual e 
# o os.kill envia a mensagem pro SO

def on_press(key):
    if key == TECLA_INTERRUTORA:
        print("\n[ESC pressionado! Encerrando cadastro...]")
        # Envia um sinal de interrupção (Ctrl+C) para destravar o input() na hora
        os.kill(os.getpid(), signal.SIGINT)
        return False  # Para o listener


listener = keyboard.Listener(on_press=on_press)
listener.start()

def montagem_de_estoque():
    produtos = []
    try:
        while True:
            produto = {}
            produto["nome"] = input("\nDigite o nome do produto:\n")
            produto["estoque"] = input("\nDigite o estoque disponível do produto:\n")
            produto["minimo"] = input("\nDigite o estoque minimo do produto:\n")
            produtos.append(produto)
    except KeyboardInterrupt:
        return produtos

def identificador_reposicao(produtos):
    produtos_em_falta = []
    for produto in produtos:
        if produto['estoque'] < produto['minimo']:
            produtos_em_falta.append(produto['nome'])
    return produtos_em_falta

def repositora(produtos):
    if len(identificador_reposicao(produtos)) > 0:
        print('Produtos que precisam de reposição:\n')
    else:
        print('Não são necessárias reposições no momento')
    for produto in identificador_reposicao(produtos):
        print(f"- {produto}")
        
repositora(montagem_de_estoque())