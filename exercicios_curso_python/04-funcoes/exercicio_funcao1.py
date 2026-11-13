import time

def monitoramento():

	inicio = time.perf_counter()
	def multiplicadora (*args):
		valor_inicial = 1
		for arg in args:
			valor_inicial *= arg
		return valor_inicial

	fim = time.perf_counter()
	print(f"Tempo de inicio: {inicio:.2f}\nTempo de fim: {fim:.2f}")
	# print(f"Tempo em minutos: ")
	return multiplicadora

resultado = monitoramento()
print(resultado(8, 94, 3, 6, 7))