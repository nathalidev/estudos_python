"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    n = int(input("Digite um n° inteiro: "))
    if n %2 == 0:
        print(f"{n} é par!")
    else:
        print(f"{n} é ímpar!")
except ValueError:
    print(f"Atenção! Digite um n° inteiro.")
except Exception as e:
    print(f"Algo deu errado!\n{e}")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    horario = input("Que horas são ('Horário:Minutos') : ").split(":")
    horario_convertido_p_inteiro = list(map(int, horario))
        
    if horario_convertido_p_inteiro[1] > 59:
        arredondar_horario = input(f"Esses minutos não existem, você quis dizer {horario_convertido_p_inteiro[0]+1}:00? (Sim / Não)")
        if arredondar_horario.lower() == 'sim':
            horario_convertido_p_inteiro[0] += 1
            horario_convertido_p_inteiro[1] = 00
        else:
            print("Digite algo válido")
        
    if 0 <= horario_convertido_p_inteiro[0] <= 11: 
        print("Bom dia!")

    elif 12 <= horario_convertido_p_inteiro[0] <= 17: 
        print("Boa tarde!")
        
    elif 18 <= horario_convertido_p_inteiro[0] <= 23: 
        print("Boa noite!")
        

    else:
        print("Seu horário não existe")
    
except Exception as e:
    print(f"Atenção! Algo deu errado\n{e}")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite o seu nome: ")
tamanho_nome = len(nome)
if tamanho_nome <= 4:
    print("Seu nome é curto")
    
elif  tamanho_nome == 5 or tamanho_nome == 6:
    print("Seu nome é normal")

else:
    print("Seu nome é muito grande")
