# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
	"""
	Decorator que envolve uma função em um wrapper.

	Fluxo:
		1. O @criar_funcao equivale a:
		inverte_string = criar_funcao(inverte_string)

		2. O decorator recebe a função original em `func`,
		cria e retorna a função `interna`.

		3. Após o retorno, `inverte_string` passa a apontar
		para `interna`.

		4. Ao chamar inverte_string('123'), na prática
		interna('123') é executada. O '123' é recebido
		em `args`.

		5. O wrapper valida os argumentos e chama a função
		original através de func(*args, **kwargs).

		6. O retorno da função original é armazenado em
		`resultado`, retornado pelo wrapper e, por fim,
		atribuído à variável que recebeu a chamada.

	`*args` recebe argumentos posicionais e `**kwargs` recebe
	argumentos nomeados, permitindo ao wrapper repassá-los
	para a função original.
	"""
	def interna(*args, **kwargs):
		print('Vou te decorar')
		for arg in args:
			e_string(arg)
		resultado = func(*args, **kwargs)
		print(f'O seu resultado foi {resultado}.')
		print('Ok, agora você foi decorada')
		return resultado
	return interna


@criar_funcao
def inverte_string(string):
	print(f'{inverte_string.__name__}')
	return string[::-1]


def e_string(param):
	if not isinstance(param, str):
		raise TypeError('param deve ser uma string')


invertida = inverte_string('123')