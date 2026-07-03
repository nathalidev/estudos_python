def criar_contador():
    total_mensagens = 0
    def adicionar(string = ""):
        nonlocal total_mensagens
        total_mensagens +=1
        print(f"\n{string}")
        print(f"\nTotal de mensagens: {total_mensagens}\n")
    return adicionar

contador = criar_contador()
while True:
    mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ")
    if mensagem.lower() == "sair":
        break
    contador(mensagem)