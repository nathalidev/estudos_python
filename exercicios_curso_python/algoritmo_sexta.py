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

def test(lista_1, lista_termos_a_serem_comparados):
    for nome, valor in {
    "lista_1": lista_1,
    "lista_termos_a_serem_comparados": lista_termos_a_serem_comparados
    }.items():
        if not isinstance(valor, list):
            raise TypeError(f"O parâmetro '{nome}' deve ser uma lista.") # aqui eu ja trato especificamente o typeerror mais se eu não soubesse qual era o erro eu dfazia um try except Exception.
# eu crio um dicionario depois pego o valor de cada campo e confiro em cada valor se é uma lista
#forma mais facil de garantir que  o usuario vai passar as duas lsitas de termo a serem comparados entre si 
    lista_que_armazena_a_resposta = []
    for termo in lista_termos_a_serem_comparados:
        termo = str(termo) #garantindo que o termo é uma string
        resposta_de_cada_comparacao = []
        for elementos in lista_1:
            elementos = str(elementos)
            resposta = elementos.count(termo)
            resposta_de_cada_comparacao.append(resposta)
            
        lista_que_armazena_a_resposta.append(resposta_de_cada_comparacao)
    return print(f"{lista_1} - {lista_termos_a_serem_comparados} -> {lista_que_armazena_a_resposta}")

test(['list', 'name', 'kkkkk'], ['k', 1, 'i', '3'])