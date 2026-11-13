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

for dicionario in perguntas:
    while True:
        print("Pergunta :", dicionario['Pergunta'])
        print("Opções:\n")
        for i, opcoes in enumerate(dicionario['Opções'], start=1):
            print(f"{i}) {opcoes}")
        try:
            opcao_usuario = int(input("Escolha uma opção: "))
            resposta_certa = dicionario["Resposta"]
            if  opcao_usuario < 1 or opcao_usuario > len(dicionario["Opções"]):
                print("Opção inválida")
                time.sleep(2)
                
            elif dicionario['Opções'][opcao_usuario-1] == resposta_certa:
                print("Parabéns, você acertou!\n")
                time.sleep(2)
                break
            
            else:
                print("Resposta incorreta\n")
                time.sleep(2)
                
        except Exception as e:
            print("Opção inválida\n")
            time.sleep(2)
