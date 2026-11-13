# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n # yield não encerra a função, só pausa nela, devolvendo um valor ao usuário

        if n >= maximum:
            return n


gen = generator(maximum=20)
for n in gen:
    print(n)

"""O generator é um tipo de iterador economico
- Ele poupa memória, ideal para grandes volumes ou fluxos contínuos de dados. 
"""