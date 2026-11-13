from typing import List, Dict, Any
from datetime import datetime
class Salas:
    def __init__(self, capacidade, recursos: List[str], reservas: List[Dict[str, Any]]):
        self.capacidade = capacidade
        self.recursos = recursos
        self.reservas = reservas

    def reservar(self, data, horario):
        reserva = {}
        reserva['Data'] = data
        reserva['Horário'] = horario
        self.reservas.append(reserva)

    def disponivel(self,reservas):
        for reserva in reservas:
            if 

data = input("Digite a data da reserva (DD/MM/AAAA): ")
try: 
    data = datetime.strptime(data, "%d/%m/%Y")
except ValueError:
    print("Data inválida. Por favor, use o formato DD/MM/AAAA.")
horario = input("Digite o horário da reserva (HH:MM): ")
try:
    horario = datetime.strptime(horario, "%H:%M").time()
except ValueError:
    print("Horário inválido. Por favor, use o formato HH:MM.")

vai_reservar = input("Deseja reservar a sala? (s/n): ")
if vai_reservar.lower() == 's':
    dia_horario_reserva 

