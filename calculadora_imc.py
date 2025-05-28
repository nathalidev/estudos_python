try:
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso/(altura**2)
    if imc < 18.5:
        print(f"Seu imc é igual a {imc:.2f}: Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        print(f"Seu imc é igual a {imc:.2f}: Peso normal")
    elif 25 <= imc <= 29.9:
        print(f"Seu imc é igual a {imc:.2f}: Sobrepeso")
    elif 30 <= imc <= 34.9:
        print(f"Seu imc é igual a {imc:.2f}: Obesidade Grau I")
    elif 35 <= imc <= 39.9:
        print(f"Seu imc é igual a {imc:.2f}: Obesidade Grau II")
    else:
        print(f"Seu imc é igual a {imc:.2f}: Obesidade Mórbida")
except Exception as e:
    print(f"Você inseriu um valor inválido:\n{e}")
    

# Abaixo do peso: imc:.2f < 18,5 kg/m².
# Peso normal: imc:.2f entre 18,5 e 24,9 kg/m².
# Sobrepeso: imc:.2f entre 25 e 29,9 kg/m².
# Obesidade: imc:.2f a partir de 30 kg/m².
# Detalhes sobre a classificação da obesidade:
# Obesidade Grau I: imc:.2f entre 30,0 e 34,9 kg/m².
# Obesidade Grau II: imc:.2f entre 35,0 e 39,9 kg/m².
# Obesidade Grau III (Obesidade Mórbida): imc:.2f a partir de 40 kg/m². 
