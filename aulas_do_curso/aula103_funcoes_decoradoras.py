# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            print(f'Checando se {arg} é uma string')
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)

# Fluxo de execução:
# 1. A função `criar_funcao` é chamada com a função `inverte_string` como argumento.
# 2. E o que criar_funcao com inverte_string no argumento retornaria? Ora de qualquer forma ela retorna a função interna, que é a função `interna`. Então, `inverte_string_checando_parametro` agora é uma referência para a função `interna`.
# 3. Quando chamamos `inverte_string_checando_parametro('123')`, estamos chamando a função `interna` com o argumento `'123'`.
# 4. Dentro da função `interna`, ele imprime "Vou te decorar", e depois entra no loop `for` para verificar se cada argumento é uma string usando a função `e_string`. 
# 5. Como `'123'` é uma string, não ocorre nenhum erro.
# 6. Em seguida, a função `func` (que é `inverte_string`) é chamada com o argumento `'123'`, e o resultado é armazenado na variável `resultado`. A função `inverte_string` retorna `'321'.
# 7. Ou seja invertida passa a ser `'321'`.