import random
itens = ["arroz", "feijão", "leite", "pão", "ovo", "café", "açúcar", "tomate"]

print("Opções disponíveis:")
contador = 1
for item in itens:
    contador +=1
    print(f"{contador}.{item}")
    
escolhidos_do_programa = []

while len(escolhidos_do_programa) < 5:
    escolhido_do_programa = random.choice(itens)
    if escolhido_do_programa not in escolhidos_do_programa:
        escolhidos_do_programa.append(escolhido_do_programa)

lista_do_usuario = input("Escolha 5 itens que você acha que estão na lista secreta: ").split(" ")

for item in lista_do_usuario:
    if item not in escolhido_do_programa:
        print("Errou!")
        break
else:
    print("Acertou!")
