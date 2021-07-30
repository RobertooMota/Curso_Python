import serial
import sys
import sqlite3
from time import sleep

bancoDados = sqlite3.connect('Teste.bd')


porta = "COM5"
baudRate = 9600
conection = serial.Serial(porta, baudRate, timeout=0.5)


def write_Serial(valor):
	conection.write(valor.encode())
	sleep(0.5)
	recebido = conection.readline().decode()
	return recebido


while True:
	entrada = input('Valor: ').upper()
	if entrada == 000:
		break
	else:
		retorno = write_Serial(entrada)
		print(f'Arduino retornou: {retorno}')

conection.close()
sys.exit()
