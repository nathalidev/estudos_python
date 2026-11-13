def lista_de_compras(nome, lista_frutas = None, *args, urgente = False):
    print(f"Nome: {nome}")
    print(f"Lista de frutas:")
    if lista_frutas:
        for fruta in lista_frutas:
            print(f"- {fruta}")
    else:
        print("Não há frutas na compra.")

    print(f"Lista de outros itens:")
    for outro_item in args:
        print(f"- {outro_item}")

    if urgente:
        print("Compra urgente")

frutas = ["maçã", "banana", "laranja", "manga", "uva"]

lista_de_compras("Nathã", None, ["arroz", "feijão", "leite"], urgente = True)

