from time import sleep
print("="*10,"Cadastramento de Produto", "="*10)
lista_produtos = []
while True:
    try:
        acao_do_usuario = int(input("\nDigite:\n1-Adicionar novos produtos\n2-Buscar um produto pelo nome\n3-Atualizar a quantidade em estoque\n4-Mostrar todos os produtos cadastrados.\nSua Opção: "))
        if acao_do_usuario == 1:
            nome = input("\nDigite o nome do produto: ")
            preco = float(input("\nDigite o preço do produto: "))
            qtd_estoque = int(input("\nDigite a quantidade em estoque: "))

            produto = {
                "Nome": nome,
                "Preço": preco,
                "Quantidade de estoque": qtd_estoque
            }


            lista_produtos.append(produto)
            
        elif acao_do_usuario == 2:
            nome_a_buscar = input("\nDigite o nome do produto a ser buscado: ")
            for produto in lista_produtos:
                if produto["Nome"] == nome_a_buscar:
                    print(f"\nResultado da busca: {produto}")
                    
        elif acao_do_usuario == 3:
            nome_a_buscar = input("Digite o nome do produto a ser buscado: ")
            for produto in lista_produtos:
                if produto["Nome"] == nome_a_buscar:
                    produto["Quantidade de estoque"] = int(input("Digite a nova quantidade de estoque desse produto: "))
                else:
                    print("Produto não encontrado.")
                    
        elif acao_do_usuario == 4:
            print("\nLista de produtos:\n")
            for produto in lista_produtos:
                print(f"{produto}")
                sleep(5)
        
        elif acao_do_usuario == 5:
            break
        
        else:
            print("Opção Inválida")
        
    except Exception as e:
        print(f"Erro inesperado: {e}")


