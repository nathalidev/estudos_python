par_ou_impar = lambda numero : numero % 2 == 0
# print(par_ou_impar(3)) funcao para mostrar se um n° é par ou impar

nomes = ["ana", "bruno", "carla"]
tudo_maiusculo = list(map(lambda nome : nome.upper(), nomes))
print(tudo_maiusculo) 

"""o map só leva aquilo que você quer aplicar a cada termo de um iterável agora o que você vai querer aplicar 
(a função) você joga ali como primeiro argumento do map e você ja aproveita para definir o que vai simbolizar cada termo 
e o iterável vai ser o segundo argumento do map"""

