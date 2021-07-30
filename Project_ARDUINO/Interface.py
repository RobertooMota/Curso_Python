from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QIcon
from time import sleep
import serial
import sys

porta = "COM5"
baudRate = 9600
conn = serial.Serial(porta, baudRate, timeout=.1)

sub = 'HELLOW WORLD'


def write_Serial(valor):
	if valor == 'L':
		lbl_imagem.setPixmap(QIcon('imgs/ligar.png').pixmap(250, 200, QIcon.Active))
	elif valor == 'D':
		lbl_imagem.setPixmap(QIcon('imgs/desligar.png').pixmap(250, 200, QIcon.Active))
	conn.write(valor.encode())
	sleep(0.5)
	recebido = conn.readline().decode()

	return recebido


class mainWindow(QWidget):
	def __init__(self):
		super().__init__()
		# Configurações da janela
		# Tamanho e posição
		self.setFixedSize(600, 600)
		self.setWindowTitle(f'Arduino: {sub}')
		self.setWindowIcon(QIcon('imgs/arduinoLogo.png'))
		self.content()

	def content(self):
		global lbl_imagem
		global statusLamp
		statusLamp = 'D'

		lbl_imagem = QLabel(self)
		# Nome OJT.FuncaoPixM(Funçao ICO(Local ICO).FuncaoPIXM(Largu, Altu, Estado da imag)
		lbl_imagem.setPixmap(QIcon('imgs/desligar.png').pixmap(250, 200, QIcon.Active))
		lbl_imagem.move(200, 200)

		btn_botao = QPushButton('Pressione Aqui', self)
		btn_botao.move(245, 430)
		btn_botao.setFixedSize(100, 30)

		btn_botao.clicked.connect(self.botaoAcao)

	def botaoAcao(self):
		global statusLamp
		if statusLamp == 'D':
			statusLamp = 'L'
		else:
			statusLamp = 'D'
		retorno = write_Serial(statusLamp)
		print(retorno)


def execution():
	app = QApplication.instance()
	if app is None:
		app = QApplication(sys.argv)
	janela = mainWindow()
	janela.show()
	app.exec()


execution()
