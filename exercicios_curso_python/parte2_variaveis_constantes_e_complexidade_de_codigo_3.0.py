RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade = 61
local_carro = 100

carro_acima_da_velocidade = velocidade > RADAR_1
'''se eu não especificar o inicio do range ele vai começar por 0 e se eu especificar um n° como inicio o range vai do meu inicio até final-1 por padrão'''
local_do_radar = list(range((LOCAL_1 - RADAR_RANGE), (LOCAL_1 + RADAR_RANGE), 1))
carro_passou_pelo_radar = local_carro in local_do_radar
carro_multado = carro_acima_da_velocidade and carro_passou_pelo_radar

if carro_acima_da_velocidade:
    print('Velocidade acima do permitido')

if carro_passou_pelo_radar:
    print('Carro passou pelo radar')

if carro_multado:
    print('Carro multado no radar')