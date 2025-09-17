try:
    numero = int(input("Digite um n°: "))

except ValueError as e:
    print(f"\nNumero inválido!\n{e}\n")

except Exception as e:
    #pra mim saber a classe do erro e tratar com mais precisão no except
    print (e.__class__.__name__) #o except mais específico sempre é verificado primeiro, e se ele capturar, os demais são ignorados.
    #esse foi ignorado

else:
    print(f"\nOK seu n° {numero} é válido\n")

finally:
    print("Fim da operação fera!\n")
# -------------------------------------------------------------------
lista = [(x,y) for x in range(1, 6) for y in range(1, 4)]
print(f"Essa é a lista de tuplas: {lista}\n")
# -------------------------------------------------------------------
def criar_multiplicador(n):
    def multiplicador(numero):
        return numero*n
    return multiplicador

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(5))
print(triplo(5))

# -------------------------------------------------------------------
try:
    x = (int(input("\nDigite um n°: ")))
    print("\nPositivo" if x > 0 else "\nNegativo" if x < 0 else "\nZero")
except ValueError as e:
    print("\nN° inválido.")


