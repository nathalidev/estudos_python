# import re 
# cpf = re.sub(r'[^0-9]', '', input("Digite um CPF: ")) dessa forma elimino tudo que não for n°

import random

cpf = []

for i in range(9):
    digito = random.randint(0, 9)
    cpf.append(digito)

multiplicador = 10
resultados_p_somar = []
for digito in cpf:
    resultados_p_somar.append(int(digito) * multiplicador)
    multiplicador -= 1
resultado = (sum(resultados_p_somar) * 10) % 11
primeiro_digito = resultado if resultado < 10 else 0
cpf.append(primeiro_digito)

dez_digitos = cpf[:10]
multiplicador = 11
resultados_p_somar = []
for digito in dez_digitos:
    resultados_p_somar.append(int(digito) * multiplicador)
    multiplicador -= 1
resultado = (sum(resultados_p_somar) * 10) % 11
segundo_digito = resultado if resultado < 10 else 0
cpf.append(segundo_digito)
cpf = map( lambda x: str(x), cpf)
cpf = "".join(cpf)
cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

print(cpf)

