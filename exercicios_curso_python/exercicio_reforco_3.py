frases = ["Python é legal", "Aprender Python é divertido", "Python Python!"]

repeticoes = {}

# eu pego cada frase da lista frases e separo em palavras atraves do split nas frases e jogo cada palavra na lista frases
frases = [palavra for frase in frases for palavra in frase.split()]

for palavra in frases:
    repeticoes[palavra] = repeticoes.get(palavra , 0) + 1 # a cada palavra adicionada na lista eu verifico o seu valor e somo + 1

print(repeticoes)

# ---------------------------------------------------------------

notas = {"Ana": 8, "Bruno": 6, "Carlos": 7, "Diana": 5}

resultado = dict(filter(lambda nota: nota[1]>=7 , notas.items()))
print(resultado) #usando filter pra filtrar ao inves do map para modificar
#  ou seja para pegar o valor seria nota[1] e o nome seria nota[0] e asism eu filtro

# ----------------------------------------------------------------
import copy
estoque = {
    "eletronicos": ["celular", "tv"],
    "moveis": ["cadeira", "mesa"]
}

copia_estoque = copy.deepcopy(estoque)

copia_estoque["eletronicos"].append("notebook") # faço uma copia do dicionario e altero o original



