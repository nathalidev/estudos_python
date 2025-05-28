try:
    n1 = int(input("Digite o 1° n° a ser comparado: "))
    n2 = int(input("Digite o 2° n° a ser comparado: "))
    
    if n1 > n2: 
        print(f'{n1} é maior que {n2}')
    elif n1 == n2:
        print(f'{n1} é igual a {n2}')
    else:
        print(f'{n2} é maior que {n1}')
except Exception as e:
    print(f'Insira valores válidos.')
