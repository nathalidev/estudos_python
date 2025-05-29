# Desenvolva uma função em python na qual poderá receber dois parâmetros de [qualquer tipo de dados].
# De acordo com o tipo de dados que entrarem como input na função, haverão comparações entre ambos.

# exemplo: test(['list', 'name', 'kkkkk'], 'k') ->  [0, 0, 5] 
# Como no exemplo mostreado acima, o segundo parâmetro deverá ser 
# comparado com cada elemento da primeira lista, verificando se a string ou o elemento 
# contém a palavra do segundo parametro.

# exemplo: test(['list', 'name', 'kkkkk'], ['k', 1, '3']) -> [[0, 0, 5], [0, 0, 0], [0, 0, 0]]
# str, list[str] !=
# str, list[str] != 

# exemplo: test('kkkkk', ['k', 1, '3']) -> [5, 0, 0]
# Caso o segundo parametro for uma lista, retorne um array de arrays, 
# na qual cada elemento do array (de dentro) deverá mostrar o match de dados.

lista1 = []

for i in range(3):
    termo_primeira_lista = input("Digite algo: ")
    lista1.append(termo_primeira_lista)
    
lista_que_armazena_a_resposta = []

quantidade_de_termos_a_comparar = int(input("Digite a quantidade de termos a serem comparados: "))

if quantidade_de_termos_a_comparar > 1:
    
    lista_termos_a_serem_comparados=[]
    
    for i in range(quantidade_de_termos_a_comparar):
        termo_a_ser_comparado = input("Digite o termo a ser comparado: ")
        lista_termos_a_serem_comparados.append(termo_a_ser_comparado)
        
    for termo in lista_termos_a_serem_comparados:
        resposta_de_cada_comparacao = []
        
        for elementos in lista1:
            resposta = elementos.count(termo)
            resposta_de_cada_comparacao.append(resposta)
            
        lista_que_armazena_a_resposta.append(resposta_de_cada_comparacao)
        
    print(f"{lista1} - {lista_termos_a_serem_comparados} -> {lista_que_armazena_a_resposta}")
    
else:
    termo_a_ser_comparado = input("Digite o termo a ser comparado: ")
    
    for termo in lista1:
        resposta = termo.count(termo_a_ser_comparado)
        lista_que_armazena_a_resposta.append(resposta)
        
    print(f"{lista1} - {termo_a_ser_comparado} -> {lista_que_armazena_a_resposta}")