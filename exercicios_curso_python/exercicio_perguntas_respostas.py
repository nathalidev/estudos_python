# Exercício - sistema de perguntas e respostas


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
    for chave, valor in dicionario.items():
        if chave == "Pergunta":
            print(chave, ":", valor)
        if chave == "Opções":
            print(chave,":")
            contador = 1
            for opcao in valor:
                print(f"{contador})", f"{opcao}")
                contador += 1
            opcao_usuario = int(input("Escolha uma opção: "))
            resposta_certa = dicionario["Resposta"]
            if (opcao_usuario -1) == valor.index(resposta_certa):
                print("Parabéns, você acertou!\n")
            else:
                print("Resposta errada...\n")