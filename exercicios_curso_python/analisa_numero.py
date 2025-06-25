numero = int(input("Digite um n°:  "))
def analisa_numero (numero):
    if  numero %2 == 0:
        par_impar = f"{numero} é par"
    else:
        par_impar = f"{numero} é ímpar"
        
    if numero == 1:
        primo = f"{numero} não é primo"
    else:
        primo = f"{numero} é primo"
        for i in range(2, numero):
            if numero % i == 0:
                primo = f"{numero} não é primo"
                break
    if numero%5 == 0:
        divisivel_por_5 = f"{numero} é divisivel por 5"
    else:
        divisivel_por_5 = f"{numero} não é divisivel por 5"
        
    resultados = {"Par ou Impar" : par_impar,
                    "É primo" : primo,
                    "É divisivel por 5" : divisivel_por_5}
    return resultados

print(analisa_numero(numero))