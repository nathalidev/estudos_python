numero = int(input("Digite um n°: "))
def par_impar (numero):
    if  numero %2 == 0:
        par_impar = f"{numero} é par"
    else:
        par_impar = f"{numero} é ímpar"
    return par_impar

def numero_primo (numero):        
    if numero == 1:
        primo = f"{numero} não é primo"
    else:
        eh_primo = True  # assume que é primo até provar o contrário
        for i in range(2, numero):
            if numero % i == 0: # no caso se um n° for divisivel de forma inteira por outro ele deixa de ser primo
                eh_primo = False
                break # a gente ja para o laço nesse caso 
        if eh_primo:
            primo = f"{numero} é primo." 
        else:
            primo = f"{numero} não é primo."# se ele não bater no if sinal de que ele iterou de 2 até o próprio n°-1 
            # sem ninguem conseguir dividir mostrando que o n° é primo 
    return primo

def divisivel_por_cinco(numero):
    if numero%5 == 0:
        divisivel_por_5 = f"{numero} é divisivel por 5"
    else:
        divisivel_por_5 = f"{numero} não é divisivel por 5"
    return divisivel_por_5
        
resultados = {"Par ou Impar" : par_impar(numero),
                "É primo" : numero_primo(numero),
                "É divisivel por 5" : divisivel_por_cinco(numero)}

for chave,valor in resultados.items():
    print(f"{chave}: {valor}")