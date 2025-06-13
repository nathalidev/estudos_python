import os
lista_usuario = []
while True:
    print("\nSelecione uma opção")
    acao_usuario = input("[i]nserir [a]pagar [l]listar [s]air: ")
    
    if acao_usuario == "i":
        os.system('clear')
        novo_item = input("\nDigite o item a ser adicionado (ou [v]oltar): ")
        if novo_item == "v":
            os.system('clear')
            continue
        lista_usuario.append(novo_item)
    
    elif acao_usuario == "a":
        if len(lista_usuario) > 0:
            while True:
                try:
                    os.system('clear')
                    indice_da_exclusao = input("\nDigite o índice do item a ser excluído (ou [v]oltar): ")
                    if indice_da_exclusao == "v":
                        continue
                    else:
                        os.system('clear')
                        int(indice_da_exclusao)
                        if indice_da_exclusao not in range(len(lista_usuario)):
                            print("\nDigite um n° válido")
                        else:
                            lista_usuario.pop(indice_da_exclusao)
                            break
                except Exception as e:
                    os.system('clear')
                    print(f"\nErro! {e}")
        
    elif acao_usuario == "l":
        os.system('clear')
        if len(lista_usuario) < 1:
            print("\nTem nada na lista ainda paizão...")
        for indice, item in enumerate(lista_usuario):
            print(indice, item)
    
    elif acao_usuario == "s":
        break
    
    else:
        print("\nDigite uma opção válida")
    