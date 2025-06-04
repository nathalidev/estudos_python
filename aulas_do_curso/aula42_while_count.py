frase = input("Digite a frase: ")
frase = frase.lower()

letras_que_mais_apareceram = [] # pro caso de nao ter uma letra em especifico que mais apareceu

i = 0
qtd_letra_que_mais_apareceu = 0
letra_apareceu_mais_vezes = ''

while i < len(frase): #eu ja tenho 0 e vou iterar enquanto ele for menor que o tamanho da minha frase
    letra_atual = frase[i]

    if letra_atual == ' ': #se a letra em questão for um espaço em branco ele só vai passar pro prox elemento da frase
        i += 1
        continue

    qtd_letra_atual_apareceu = frase.count(letra_atual) #vai pegar quantas vezes a letra atual apareceu na frase 

    i += 1 #soma mais um ao iterador, até percorrer o tamanho da frase e voce sair do laço
    
    if qtd_letra_que_mais_apareceu < qtd_letra_atual_apareceu: #inicialmente voce compara com 0 depois voce compara com a letra que mais apareceu na frase até aquele momento
        qtd_letra_que_mais_apareceu = qtd_letra_atual_apareceu #se a letra atual apareceu mais vezes que a anterior ocorre a reatribuição
        letra_apareceu_mais_vezes = letra_atual #e então a letra que mais apareceu se torna a atual
        
        
    elif qtd_letra_que_mais_apareceu == qtd_letra_atual_apareceu:
        letras_que_mais_apareceram.append(letra_atual)
        
if len(letras_que_mais_apareceram) > 1:
    print(
        'As letras que apareceram mais vezes foram '
        f'"{",".join(letras_que_mais_apareceram)}" que apareceram '
        f'{qtd_letra_que_mais_apareceu}x'
    )

else:
    print(
        'A letra que apareceu mais vezes foi '
        f'"{letra_apareceu_mais_vezes}" que apareceu '
        f'{qtd_letra_que_mais_apareceu}x'
    )
