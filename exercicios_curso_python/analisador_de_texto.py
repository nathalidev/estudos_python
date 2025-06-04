frase = input("Digite uma frase: ")
frase_sem_espaco = frase.replace(" ", "")
palavras_da_frase = frase.split(" ")
numero_de_palavras = len(palavras_da_frase)

print(f"N° de palavras: {numero_de_palavras}")

numero_caracteres = len(frase)
print(f"N° de caracteres (contando espaços) na frase: {numero_caracteres}")

for letra in set(frase_sem_espaco): # a cada letra (sem repetida) dentro da frase sem contar os espaços eu terei um contador
    contador_de_letras = 0
    for l in frase_sem_espaco : #a cada letra da frase sem espaço 
        if l == letra: # se ela bater com a letra sem repetição o contador daquela letra vai somar +1
            contador_de_letras += 1
    print(f"{letra} aparece {contador_de_letras} vezes na frase")

# for letra in set(frase_sem_espaco): poderia ter feito assim no trecho final
#     contador_de_letras = frase_sem_espaco.count(letra) 
#     print(f"{letra} aparece {contador_de_letras} vezes na frase")
    
# 1 - eu iria de letra em letra na frase sem espaço e sendo set não teriam termos repetidos
# 2 - a cada letra sem ser repetida eu conto quantas vezes ela aparece na frase sem espaço
