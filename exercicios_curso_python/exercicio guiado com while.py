nome = input(("Digite o nome: "))
tamanho_do_nome = len(nome)

contador = 0
nome_com_asteriscos = ""
while contador < tamanho_do_nome:
    nome_com_asteriscos += "*" + nome[contador]
    if contador == tamanho_do_nome-1:
        nome_com_asteriscos += "*"
    contador +=1
print(nome_com_asteriscos)
