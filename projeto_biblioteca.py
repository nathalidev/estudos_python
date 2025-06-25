from time import sleep
from datetime import datetime

ano_atual = datetime.now().year

print("Inicializando...")
sleep(2)

titulo_do_sistema = "="*6+"Biblioteca Virtual"+"="*6
print("\n"+titulo_do_sistema.center(150)) #titulo centralizado com o center(), \n buga tudo se estiver dentro da variavel do titulo

lista_livros = []
while True:
    try:
        titulo_do_livro = input("Qual o título do livro que você deseja adicionar: ")
        autor = input("Qual o autor do livro que deseja adicionar: ")
        ano_do_livro = int(input("Qual o ano de lançamento do livro: "))
        genero_do_livro = input("Qual o gênero do livro que deseja adicionar: ")
        status_do_livro = input("O livro que está adicionando ja foi lido? [S/N] ")
        
        if ano_do_livro > ano_atual:
            break
        
        else:
            lista_livros.append({"Titulo do livro" : titulo_do_livro,
                                "Autor" : autor,
                                "Ano de lançamento" : ano_do_livro,
                                "Gênero do livro" : genero_do_livro,
                                "Status de leitura" : status_do_livro})

    except Exception as e:
        print(f"Erro: {e}")
        
mostrar_livros = input("Mostrar os livros? [S/N] ")
if mostrar_livros.upper() == "S":
    print(lista_livros)


