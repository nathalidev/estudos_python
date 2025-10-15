# 1️⃣ Manipulação de strings e contagem de padrões
# Crie uma função que recebe um texto e retorna um dicionário com:

# Número de palavras com mais de 5 letras

# Número de palavras que começam e terminam com a mesma letra

# A palavra mais longa do texto

def contagem_padroes (texto):
    palavras = texto.strip('.,!?').split()
    palavras_5letras = []
    n_palavras_5_letras = 0
    palavras_comeco_igual_fim = []
    n_palavras_comeco_igual_fim = 0
    respostas = {"Palavras com mais de 5 letras": "", "Palavras que começam e terminam com a mesma letra": ""}
    for palavra in palavras:
        if len(palavra) > 5:
            n_palavras_5_letras +=1 
            palavras_5letras.append(palavra)
        if palavra[0] == palavra[-1]:
            n_palavras_comeco_igual_fim +=1
            palavras_comeco_igual_fim.append(palavra)

    if len(palavras_5letras) == 0:
        palavras_5letras.append("Nehnuma")

    if len(palavras_comeco_igual_fim) == 0:
        palavras_comeco_igual_fim.append("Nehnuma")


    respostas["Palavras com mais de 5 letras"] = n_palavras_5_letras
    respostas["Palavras que começam e terminam com a mesma letra"] = n_palavras_comeco_igual_fim
    return f"{respostas}\nAs palavras com mais de cinco letras são: {palavras_5letras}\nAs palavrasPalavras que começam e terminam com a mesma letra são: {palavras_comeco_igual_fim}"

print(contagem_padroes("Eu gosto de jogar futebol!"))

