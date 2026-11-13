# 2️⃣ Processamento de números e lógica
# Faça uma função que recebe uma lista de números inteiros e retorna uma nova lista com:

# Apenas números primos

# Cada número primo multiplicado pelo índice dele na lista original

# Exemplo de assinatura:

def primos_indexados(numeros):
    if not isinstance(numeros, list):
        print("ATENÇÃO: Você deve passar uma lista como parâmetro...")
        return
    numeros_primos = []
    numeros_primos_modificados = []
    for numero in numeros:
        if numero> 1:
            primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break
            if primo:
                numeros_primos.append(numero)

    for numero in numeros_primos:
        indice = numeros.index(numero)
        numero_primo_modificado = numero*indice
        numeros_primos_modificados.append(numero_primo_modificado)

    respostas = {"Numeros primos": numeros_primos, "Numeros primos modificados": numeros_primos_modificados}
    return respostas

print(primos_indexados([2, 4, 6, 8, 64, 41, 23, 10, 11]))





