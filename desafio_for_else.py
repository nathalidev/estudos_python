# Peça um número ao usuário.

# Use um for para verificar se ele é divisível por algum número entre 2 e ele mesmo.

# numero = int(input("Digite um n° e descubra se ele é primo: "))
# for i in range(2, numero):
#     if numero%i ==0:
#         print("Não é primo amigo!")
#         break
# else:
#     print("É primo irmão!!")
    
# 🔁 Desafio 2 — Adivinhação com while-else
# 📌 Objetivo: O usuário tem 3 tentativas pra adivinhar um número secreto.

import random

numero_secreto = random.randint(1, 10)
tentativas = 3
while tentativas > 0:
    palpite = int(input("Tente acertar o n° secreto: "))
    if palpite != numero_secreto:
        tentativas -= 1
        print(f"Errou fera, agora você tem {tentativas} tentativas.")
    else:
        print("Acertou malandro!")
        break
else:
    print(f"Já era, acabaram as tentativas!")