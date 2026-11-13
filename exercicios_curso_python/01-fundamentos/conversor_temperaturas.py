print("Escolha sua unidade de medida de temperatura!")
try:
    medida_da_temperatura = int(input("Digite:\n[1] para Celsius\n[2] para Fahrenheit\n[3] para Kelvin\nResposta: "))

    if medida_da_temperatura not in [1,2,3]:
        print("Digite um valor válido.")
        exit()
        
    temperatura = float(input("Digite a temperatura: "))

    convertido_para1 = ""
    convertido_para2 = ""


    temperatura_convertida_para_1 = ""
    temperatura_convertida_para_2 = ""

    simbolo_da_conversao_1 = ""
    simbolo_da_conversao_2 = ""

    if medida_da_temperatura == 1:
        simbolo = "C°"
        convertido_para1 = 'Kelvin'
        convertido_para2 = 'Fahrenheit'
        temperatura_convertida_para_1 = temperatura + 273.15
        temperatura_convertida_para_2 = 9/5 * temperatura + 32
        simbolo_da_conversao_1 = "K°"
        simbolo_da_conversao_2 = "F°"
        
    elif medida_da_temperatura == 2:
        simbolo = "F°"
        convertido_para1 = 'Celsius'
        convertido_para2 = 'Kelvin'
        temperatura_convertida_para_1 = (temperatura-32) *5/9
        temperatura_convertida_para_2 = (temperatura - 32) * 5/9 + 273.15
        simbolo_da_conversao_1 = "C°"
        simbolo_da_conversao_2 = "K°"
        
    else:
        simbolo = "K°"
        convertido_para1 = 'Celsius'
        convertido_para2 = 'Fahrenheit'
        temperatura_convertida_para_1 = temperatura - 273.15
        temperatura_convertida_para_2 = (temperatura - 273.15) * 9/5 + 32
        simbolo_da_conversao_1 = "C°"
        simbolo_da_conversao_2 = "F°"

    print(f"Sua temperatura: {temperatura}"+f"{simbolo}\nEm {convertido_para1}: {temperatura_convertida_para_1:.1f}"+f"{simbolo_da_conversao_1}\nEm {convertido_para2}: {temperatura_convertida_para_2:.1f}"+f"{simbolo_da_conversao_2}")
except Exception as e:
    print(f"Deu ruim: {e}")
#() - ** - 	*, /, //, % - + e -