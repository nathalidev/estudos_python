# Exercício - sistema de perguntas e respostas

import time

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

indice_respostas = ['A', 'B', 'C', 'D']

for pergunta in perguntas:
    
    contador_indice = 0
    
    print(f"\n{pergunta['Pergunta']}")
    
    time.sleep(2)
    
    for opcao in pergunta['Opções']:
    
        print(f"\n{indice_respostas[contador_indice]}){opcao}\n")
    
        contador_indice += 1; 
    
        time.sleep(2)
    
    while True:
    
        resposta_user = input("Insira a letra que mostra a sua resposta:\n")
    
        if resposta_user.upper() in indice_respostas:
    
            indice_resposta_user = indice_respostas.index(resposta_user.upper())
    
            indice_resposta_certa = pergunta["Opções"].index(pergunta["Resposta"])
    
            if indice_resposta_user == indice_resposta_certa:
    
                print("\nResposta certa lenda viva!")
    
                break
    
            else:
    
                print("\nErrou malandro!")
    
                break
    
        else:
    
            print("\nInsira uma resposta válida fera!")
    
        print("-"*20)
    
        time.sleep(2)


