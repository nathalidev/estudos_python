nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / altura**2

print(f"{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}")
print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu imc é',imc)