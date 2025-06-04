"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas: #enquanto 1 for menor ou igual a 5 voce cria a variavel coluna = 1 então vou ter 5 colunas
    coluna = 1
    while coluna <= qtd_colunas: #enquanto coluna for menor ou igual a 5 eu mostro os dois e somo mais uma ou seja
        print(f"{linha=}, {coluna=}") # 1,1 - 1,2 - 1,3- 1,4- 1,5- 2,1 - 2,2
        #primeiro executa o laço interno depois voce completa uma iteração do laço externo
        coluna+= 1
    
    linha += 1
    
print("Acabou")