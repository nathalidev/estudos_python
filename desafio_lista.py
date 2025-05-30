import re
import time

while True:
    valores = input("Usando espaço ou ',' como separador informe 5 valores: ")
    lista = re.split(r'[ ,]+', valores)
    if len(lista)>5 and len(lista)!= 6:
        print("\nQue isso irmão?! Lista muito grande diminui ai pra 5 elementos")
        time.sleep(2)
    if len(lista) == 6:
        print("\nIrmão você passou do limite de 5 elementos mais vou te ajudar...")
        time.sleep(2)
        print("\nO último elementos digitado vai ser removido, ta de boa?")
        continuar = input("Digite 1 para SIM qualquer outro dígito será considerado NÃO: ")
        
        if continuar == "1":
            del lista[-1]
            maior = max(lista)
            menor = min(lista)
            for indice , valor in enumerate(lista):
                if valor == maior:
                    print(f"O maior valor é o:\nIndice: {indice} - Valor: {valor}\n")
                    
                if valor == menor:
                    print(f"\nO menor valor é o:\nIndice: {indice} - Valor: {valor}\n")
            print(f"\nLista completa: {lista}")
            break
            
        
        else: 
            print("\nOk, vamos começar de novo...")
            time.sleep(2)


# lista = []
# continuar = True
# while continuar:
#     valor = input("Digite um valor para ser armazenado: ")
#     if valor not in lista:
#         lista.append(valor)
#     else:
#         print("Valores repetidos não serão adicionados...")
#     while True:
#         continua = input("Quer continuar? [S/N] ")
#         if continua.lower() == 'n':
#             print(lista)
#             continuar = False
#             break
#         elif continua.lower() == 's':
#             break