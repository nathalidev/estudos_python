from unidecode import unidecode
from time import sleep
palavra_secreta = unidecode("Gostosura")

palavra_secreta_transformada = "*" * len(palavra_secreta)

palavra_mostrada_usuario = ""

print("\nBora jogar um jogo...")
sleep(2)
print("\nA parada é o seguinte, advinhação...")
sleep(2)
print("\nA senhorita é uma...")
sleep(2)
from time import sleep
while "*" in palavra_secreta_transformada:
    letra_do_usuario = unidecode(input("Digite uma letra: "))

    if len(letra_do_usuario) > 1:
        print("\nDigite apenas uma letra.")
    else:
    
        if letra_do_usuario.lower() in palavra_secreta.lower():
            print("\nAcertei, to quase...")
            sleep(2)
            palavra_secreta_transformada = list(palavra_secreta_transformada)
            for i, letra in enumerate(palavra_secreta.lower()):
                if letra == letra_do_usuario.lower():
                    palavra_secreta_transformada[i] = palavra_secreta[i]
                
        else:
            print("\nErrou no palpite fera!, Bora lá tenta de novo...")
            sleep(2)
    
    palavra_secreta_transformada = "".join(palavra_secreta_transformada)
    print(f"\nA senhorita é uma...\n{palavra_secreta_transformada}\n")
    print("="*15+"\n")

else:
    print("\nFim de jogo besta enjaulada!")
    print(f"\nA senhorita é uma...\n{palavra_secreta_transformada}\n")
    sleep(2)
    print("Depois ainda tenho coragem de dizer que meu emprego ta me matando...")
