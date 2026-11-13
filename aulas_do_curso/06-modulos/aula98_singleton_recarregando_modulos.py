import importlib

import aula98_modularizacao

print(aula98_modularizacao.variavel)

for i in range(10):
    importlib.reload(aula98_modularizacao)
    print(i)

print('Fim')