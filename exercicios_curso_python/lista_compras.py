import keyboard
produtos = []
while True:
    produtos_em_maiusculo = [produto.upper() for produto in produtos]
    opcao = input('\nSelecione uma opção:\n[I]nserir [A]pagar [L]istar [E]ditar: \n')
    if opcao.upper() == 'I':
        nome = input('\nDigite o nome do produto:\n')
        if nome.isnumeric():
            print("\nSeu produto não pode ser apenas números seu maluco!\n")
        else:
            produtos.append(nome.strip())

    elif opcao.upper() == 'A':
        a_ser_apagado = input('Digite o nome do produto a ser apagado da lista:\n')
        if a_ser_apagado.upper() in produtos_em_maiusculo:
            indice = produtos_em_maiusculo.index(a_ser_apagado.upper())
            produtos.pop(indice) #remove remove item de uma lista pelo valor pop pelo indice

    elif opcao.upper() =='L':
        print("\n"+"="*3 +"Lista de produtos:"+"="*3)
        if len(produtos) == 0:
            print("Não há produtos na lista!")
        for i, item in enumerate(produtos):
            print(f"{i+1} - {item}") 

    elif opcao.upper() =='E':
        for i, item in enumerate(produtos):
            print(f"{i+1} - {item}")
        
        a_ser_editado = input("Digite o nome do produto a ser editado:\n")
        if a_ser_editado.upper() in produtos_em_maiusculo:
            indice = produtos_em_maiusculo.index(a_ser_editado.upper())
            nome_novo = input("Qual o nome do produto:\n")
            produtos[indice] = nome_novo
        else:
            print("\nMeu consagrado, esse produto não existe!\n")

    else:
        print("\nOpção inválida fera!\n")

        
