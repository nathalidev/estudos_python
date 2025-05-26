RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade = 61
local_carro = 100

carro_acima_da_velocidade = velocidade > RADAR_1
inicio_do_radar = LOCAL_1 - RADAR_RANGE
final_do_radar  = LOCAL_1 + RADAR_RANGE
carro_passou_pelo_radar = local_carro >= inicio_do_radar and local_carro <= final_do_radar
carro_multado = carro_acima_da_velocidade and carro_passou_pelo_radar

if carro_acima_da_velocidade:
    print('Velocidade acima do permitido')

if carro_passou_pelo_radar:
    print('Carro passou pelo radar')

if carro_multado:
    print('Carro multado no radar')