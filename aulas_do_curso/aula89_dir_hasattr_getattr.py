# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)

# for metodo in dir(string):
#     print(metodo)

# dir(obj) → lista todos os atributos e métodos disponíveis no objeto.

# hasattr(obj, "nome") → checa se o objeto tem aquele atributo/método (retorna True ou False).

# getattr(obj, "nome") → pega o atributo/método pelo nome (string). Se for método, você ainda pode chamar com ().

