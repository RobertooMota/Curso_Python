import serial

try:

	conn = serial.Serial("COM5", 9600, timeout=0.5)
	while True:
		leitura = conn.readline().decode()
		print(leitura)
		if leitura == '5':
			break


except:
	print('Falha de conexão!')
