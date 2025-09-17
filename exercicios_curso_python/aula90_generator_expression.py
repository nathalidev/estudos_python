import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
import sys

# Lista e generator expression
lista = [n for n in range(10)]           # cria todos os valores na memória
generator = (n for n in range(10))       # gera os valores sob demanda
"""
Tem duas formas principais de criar um generator em Python:

1. Usando generator expressions:
   - Parecida com list comprehension, mas usa parênteses em vez de colchetes.
   - Útil quando você tem **uma grande quantidade de dados** e não quer armazenar tudo na memória.
   - Exemplo: generator = (n for n in range(1000000))

2. Usando uma função com a palavra-chave yield:
   - Permite criar um generator personalizado.
   - A função "pausa" em cada yield, gerando os valores sob demanda.
"""

# Segunda forma: generator usando yield
def numeros_com_yield(n):
    for i in range(n):
        yield i   # cada chamada ao generator produz o próximo valor sem armazenar todos
    return
        #aqui o for é necessário porque gerando o generator dessa forma ele precisa iterar sobre alguma coisa pra gerar o generator prévio de cada termo

generator_yield = numeros_com_yield(10)

# Demonstração: iterando sobre generator expression
print("Iterando generator expression:")
for n in generator:
    print(n)

print("\nIterando generator com yield:")
for n in generator_yield:
    print(n)
    