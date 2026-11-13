def apresentar (*args, **kwargs):
    for nome in args:
        print(f"Nome: {nome}")
    
    for chave, valor in kwargs.items(): # items é necessário para trazer os valores tambem se não só é trazido as chaves
        print(f"{chave}: {valor}")

apresentar("Nathã", "Yasmin", idade=23, idade2=21, cidade="Valinhos", cidade2="Sousas")

#.keys() traz só chaves se quiser e o .values() traz só valores

