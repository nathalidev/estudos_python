import re

numeros = input("Digite os números separados por vírgula, espaço ou ponto e vírgula: ")

def gerando_media(numeros):
    try:
        lista_numeros = re.split(r'[,\s;]+', numeros.strip()) #por padrão não precisa colocar espaço no strip como argumento
        lista_numeros = list(map(int, lista_numeros)) #o map voce aplica uma função a todo termo de uma lista, map nao devolve uma lista

        lista_pesos_numeros = []
        soma_numeros_vezes_pesos = 0 #definição de variaveis é sempre feita for de laços de repetição
        numeros_multiplicados = 1

        for numero in lista_numeros:
            # print(type(numero))
            peso_do_numero = int(input(f"\nDigite o peso do n° {numero}: "))
            
            lista_pesos_numeros.append(peso_do_numero)
            
            soma_numeros_vezes_pesos += (numero*peso_do_numero)
            
            numeros_multiplicados *= numero
            
        soma_dos_numeros = sum(lista_numeros)

        media_aritmetica = soma_dos_numeros/len(lista_numeros)

        media_ponderada = soma_numeros_vezes_pesos/sum(lista_pesos_numeros)

        media_geometrica = numeros_multiplicados ** (1/(len(lista_numeros)))
        
        return f"\nN°s informados: {lista_numeros}\nMédia aritmética: {media_aritmetica:.2f}\nMédia ponderada: {media_ponderada:.2f}\nMédia geométrica: {media_geometrica:.2f}"
    except Exception as e:
        return f"Erro: {e}"


print(gerando_media(numeros))



