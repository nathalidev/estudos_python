from random import randint
num_escolhido = randint(1,12)
print("Jogo da advinhação! Tente advinhar o n° que o computador pensou...")
while True:
    palpite = int(input("\nDigite o seu palpite: "))

    if palpite == num_escolhido:
        print("\nExtouro no norte! Acertou o palpite")
        break

    elif palpite > num_escolhido:
        print("\nCalma rapaz que palpite alto é esse?!")

    elif palpite < num_escolhido:
        print("\nBora aumenta esse palpite!")

