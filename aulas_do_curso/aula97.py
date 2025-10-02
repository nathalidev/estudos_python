# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula97_modularizacao
from aula97_modularizacao import soma, variavel_modulo

# print('Este módulo se chama', __name__)
print(aula97_modularizacao.variavel_modulo)
print(variavel_modulo)
# -------------- as duas linhas acima e abaixo são iguais só mudam sintaticamente
print(soma(2, 3))
print(aula97_modularizacao.soma(2, 3))

# se eu for importar modulos que hierarquicamente estão acima ou em outro lugar eu vou ter que manipular o sys.path