continuar_calculando = True

while continuar_calculando: 
    try: 
        numero_1 = float(input("Digite um n°: "))
        numero_2 = float(input("Digite um n°: "))
        operadores_disponiveis = ["+", "-", "/", "%", "*", "**"]
        
        print(f"\nOperadores disponíveis: {operadores_disponiveis}")
        
        operador_invalido = True
        
        while operador_invalido:
            operador_da_conta = input("Informe o operador do cálculo: ")
            if operador_da_conta not in operadores_disponiveis:
                print("Informe um operador disponível")
            else:
                operador_invalido = False
                if operador_da_conta == "+":
                    resultado = numero_1 + numero_2
                    
                elif operador_da_conta == "-":
                    resultado = numero_1 - numero_2
                    
                elif operador_da_conta == "/":
                    resultado = numero_1 / numero_2
                    
                elif operador_da_conta == "%":
                    resultado = numero_1 % numero_2
                    
                elif operador_da_conta == "*":
                    resultado = numero_1 * numero_2
                    
                elif operador_da_conta == "**":
                    resultado = numero_1 ** numero_2
                    
                opcao_de_continuar_invalida = True
                
                print(f"{numero_1} {operador_da_conta} {numero_2} = {resultado:.2f}")
                
                print(f"Resultado = {resultado:.2f}")
                
                while opcao_de_continuar_invalida:
                    encerrar = input("Deseja encerrar [s|n]: ")
                    encerrar =encerrar.lower()
                    
                    if encerrar == "s" or encerrar == "sim":
                        opcao_de_continuar_invalida = False
                        continuar_calculando = False
                        
                    elif encerrar == "n" or encerrar == "nao" or encerrar == "não":
                        opcao_de_continuar_invalida =  False
                    else:
                        print("Digite uma opção válida")
    except Exception as e:
        print(f"Atenção! {e}")




