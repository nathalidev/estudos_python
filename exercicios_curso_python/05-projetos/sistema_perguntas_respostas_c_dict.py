quiz = {
	"Em que ano foi realizada a primeira Copa do Mundo de futebol?" : 1930,
	"Quem é o maior artilheiro da história das Copas do Mundo?" : "Miroslav Klose",
	"Qual seleção tem mais títulos de Copa do Mundo?" : "Brasil",
	"Qual foi o primeiro clube campeão do Campeonato Brasileiro em 1971?" : "Atlético Mineiro",
	"Qual é o maior estádio de futebol do mundo em capacidade?" : "Rungrado 1º de Maio",
	"Quantas Copas do Mundo Pelé venceu?" : 3,
	"Qual seleção venceu a primeira Eurocopa em 1960?" : "União Soviética",
	"Qual é considerada a maior rivalidade do futebol brasileiro?" : "Flamengo x Fluminense",
	"Quantos títulos de Champions League Cristiano Ronaldo conquistou?" : 5,
	"Quem marcou o primeiro gol da história das Copas do Mundo?" : "Lucien Laurent"
}

alternativas = {
	1 : [1924, 1934, 1930, 1942],
	2 : ["Ronaldo Fenômeno", "Lionel Messi", "Just Fontaine", "Miroslav Klose"],
	3 : ["Alemanha", "Itália", "Argentina", "Brasil"],
	4 : ["São Paulo", "Palmeiras", "Internacional", "Atlético Mineiro"],
	5 : ["Maracanã", "Camp Nou", "Wembley", "Rungrado 1º de Maio"],
	6 : [2, 4, 5, 3],
	7 : ["França", "Espanha", "Alemanha Ocidental", "União Soviética"],
	8 : ["Corinthians x Palmeiras", "Grêmio x Internacional", "Vasco x Flamengo", "Flamengo x Fluminense"],
	9 : [3, 6, 2, 5],
	10 : ["Guillermo Stábile", "Héctor Scarone", "Obdulio Varela", "Lucien Laurent"]
}

def quiz_futebol(quiz, alternativas):
	pontuacao = 0
	for i, (chave, valor) in enumerate(quiz.items(), start=1):
		print(f"{chave}\n")
		for indice, alternativa in enumerate(alternativas[i], start=1):
			print(f"{indice}) {alternativa}")
		
		# Agora só pergunta uma vez por questão
		resposta = input("Qual sua resposta? ")

		if resposta.isdigit():
			resposta_indice = int(resposta)
			if alternativas[i][resposta_indice - 1] == valor:
				print("Parabéns você acertou!\n")
				pontuacao += 10
			else:
				print("Errou irmão!\n")
		else:
			if resposta.lower() == str(valor).lower():
				print("Parabéns você acertou!\n")
				pontuacao += 10
			else:
				print("Errou irmão!\n")
	print(f"Pontuação final: {pontuacao}")

quiz_futebol(quiz, alternativas)

"""
	Executa um quiz de futebol com perguntas e alternativas.

	Fluxo da função:
	1. Inicializa a variável `pontuacao` com 0, que será usada para acumular os pontos do jogador.
	2. Percorre o dicionário `quiz` usando `enumerate`:
	- `i` é o índice da pergunta (começa em 1 por causa do parâmetro `start=1`).
	- `chave` é o texto da pergunta.
	- `valor` é a resposta correta daquela pergunta.
	3. Para cada pergunta:
	- Exibe o texto da pergunta (`chave`).
	- Percorre a lista de alternativas correspondente àquela pergunta (`alternativas[i]`).
		- `indice` é o número da alternativa (começa em 1).
		- `alternativa` é o texto ou número da opção.
		- Imprime cada alternativa numerada para o jogador escolher.
	- Após mostrar todas as alternativas, pede a resposta do jogador com `input`.
	4. Verificação da resposta:
	- Se o jogador digitou apenas números (`resposta.isdigit()`):
		- Converte a resposta para inteiro (`resposta_indice`).
		- Usa esse número para acessar a alternativa escolhida dentro da lista (`alternativas[i][resposta_indice - 1]`).
		- Compara com a resposta correta (`valor`).
		- Se for igual, imprime mensagem de acerto e soma 10 pontos.
		- Caso contrário, imprime mensagem de erro.
	- Se o jogador digitou texto:
		- Converte a resposta para minúsculas e compara com a resposta correta também em formato de string.
		- Se forem iguais, imprime mensagem de acerto e soma 10 pontos.
		- Caso contrário, imprime mensagem de erro.
	5. Depois de todas as perguntas, imprime a pontuação final acumulada.

	Parâmetros:
	- quiz (dict): dicionário com perguntas como chave e respostas corretas como valor.
	- alternativas (dict): dicionário com listas de alternativas para cada pergunta, indexadas por número.

	Retorno:
	- Não retorna nada. Exibe mensagens no console e a pontuação final ao término do quiz.
	"""