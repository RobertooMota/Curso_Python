from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QFrame
from PySide6.QtGui import QIcon, QFont
from datetime import date
import janela2 as p
import sys

version = 'v1.0.0'


class mainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle(f'MU1000 - {version}')

		# Criando uma instancia entre um objeto e a fonte a ser usada
		fonte = QFont('fonts/Kanit-Medium.ttf')
		fonte.setPointSize(10)
		lbl_data = QLabel(f'{date.today()}', self)
		lbl_data.move(720, 480)
		lbl_data.setFont(fonte)

		# Criando um objeto do tipo icon
		iconeJanela = QIcon('../imgs/logoJanela.png')
		# Aplicando o icone na janela
		self.setWindowIcon(iconeJanela)
		# Definindo o tamanho da janela ao abrir
		self.setFixedSize(800, 500)
		# Definindo o background da janela
		self.setAutoFillBackground(True)
		self.setStyleSheet('background-color: #light-gray')
		self.tituloJanelaPrincipal()
		self.botaoReferenciar()

	def tituloJanelaPrincipal(self):
		global lbl_Titulo

		# Criando uma instancia entre um objeto e a fonte a ser usada
		fonteTitulo = QFont("fonts/Qahiri/Qahiri-Regular.ttf")
		fonteTitulo.setPointSize(40)

		# Criando uma label
		lbl_Titulo = QLabel('MU1000', self)
		lbl_Titulo.move(220, 20)
		lbl_Titulo.setFont(fonteTitulo)
		lbl_Titulo.setStyleSheet("background-color: rgb(10,30,102);"
								 "color: white;"
								 "border-radius: 10;"
								 "padding: 5 50 5 50;")

	def botaoReferenciar(self):
		fonteBotao = QFont("fonts/Eczar/Eczar-Medium.ttf")
		fonteBotao.setPointSize(20)
		btn_botaoReferenciar = QPushButton('Entrar', self)
		btn_botaoReferenciar.setFixedSize(200, 80)
		btn_botaoReferenciar.setFont(fonteBotao)
		btn_botaoReferenciar.move(300, 200)
		btn_botaoReferenciar.setAutoFillBackground(True)
		btn_botaoReferenciar.clicked.connect(self.clickBotao)

	def clickBotao(self):
		info = QMessageBox.question(self, 'Confirmação', 'Deseja entrar?',
									QMessageBox.Yes | QMessageBox.No)
		if info == QMessageBox.Yes:
			self.close()

		if info == QMessageBox.No:
			lbl_Titulo.setStyleSheet("background-color: rgb(10,30,102);"
									 "color: white;"
									 "border-radius: 10;"
									 "padding: 5 50 5 50;")
			print('Clicou em No')

			icoNotConfirm = QIcon('../imgs/NOTOK.png')
			confirm = QMessageBox()

			confirm.setWindowTitle('Confirm')
			confirm.setWindowIcon(icoNotConfirm)
			confirm.setFixedSize(600, 200)

			confirm.setText('Não entrou')
			confirm.exec()


def execution():
	aplicativo = QApplication.instance()

	if aplicativo is None:
		aplicativo = QApplication(sys.argv)

	janelaPrincipal = mainWindow()
	janelaPrincipal.show()
	aplicativo.exec()
	return 'open janela 2'


execution()
