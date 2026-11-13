def criar_contador():
    total_mensagens = 0
    def adicionar(string = ""):
        nonlocal total_mensagens
        total_mensagens +=1
        print(f"\n{string}")
        print(f"\nTotal de mensagens: {total_mensagens}\n")
    return adicionar

contador = criar_contador()
print(contador.__code__.co_freevars) # nome da variavel livre
print(contador.__closure__) # endereço de memória de cada cell que contem uma variavel livre da closure alem do tipo e do endereço de memória do objeto que esse endereço referencia
print(locals()) # variáveis do escopo atual
print(globals()) # variáveis do escopo global
while True:
    mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ")
    if mensagem.lower() == "sair":
        break
    contador(mensagem)