from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFrame
from PySide6.QtGui import QIcon, QFont

import sys

# Versão
version = '1.0.0'

# Dimensão da janela principal
janelaWSize = 1000
janelaHSize = 700

# Dimensão padrão dos botões
botaoWSize = 240
botaoHSize = 100
offSetBotaoPrincila = 20

# Variavel para armazenar a fonte usada nos botões
fonteBotao = QFont()
fonteBotao.setFamilies([u"Montserrat"])
fonteBotao.setPointSize(16)

# Variaveis para posicionamento dos frames
frameHSize = 440
frameWSize = janelaWSize
frameXPosition = 0
frameYPosition = janelaHSize - frameHSize


class janelaPrincipal(QWidget):
	def __init__(self):
		super().__init__()
		# Formatação da janela principal
		# Tamanho e posicionamento
		self.setFixedSize(janelaWSize, janelaHSize)
		# Titulo
		self.setWindowTitle(f'MU1000 - v{version}')
		# Cor da janela
		self.setAutoFillBackground(True)
		self.setStyleSheet("background-color: rgb(237, 237, 237);")
		# Icone
		iconeJanelaPrincipal = QIcon('_imgs/logoJanela.png')
		self.setWindowIcon(iconeJanelaPrincipal)
		self.construcaoJanela()
		self.framesJanelaPrincipal()

		# -------------BOTOES-------------------
		self.botoesJanelaPrincipal()

		# -------------FRAMES-------------------
		self.framesJanelaPrincipal()

	def construcaoJanela(self):
		# Titulo da janela
		# Fonte
		fonteTitulo = QFont()
		fonteTitulo.setFamilies([u"Impact"])
		fonteTitulo.setPointSize(70)

		# Titulo
		lbl_titulo = QLabel('MU1000', self)
		lbl_titulo.move(15, 20)
		lbl_titulo.setFont(fonteTitulo)
		lbl_titulo.setStyleSheet("background-color: rgb(224, 181, 61);"
								 "color: rgb(46, 79, 230);"
								 "border-radius: 10;"
								 "padding-left: 310;"
								 "padding-right: 310;"
								 "border: 1px solid black")

	def botoesJanelaPrincipal(self):
		# Configuração do botão para usar a configuração global
		global fonteBotao

		# Instanciando o objeto a classe
		btn_botaoImprimir = QPushButton('Imprimir', self)
		btn_botaoImprimir.setFont(fonteBotao)
		btn_botaoImprimir.setGeometry(offSetBotaoPrincila, 150, botaoWSize, botaoHSize)

		btn_botaoImprimir.clicked.connect(self.exibirFrameImprimir)

		# Instanciando o objeto a classe
		btn_botaoReferenciar = QPushButton('Referenciar', self)
		btn_botaoReferenciar.setFont(fonteBotao)
		btn_botaoReferenciar.setGeometry(offSetBotaoPrincila + botaoWSize, 150, botaoWSize, botaoHSize)

		btn_botaoReferenciar.clicked.connect(self.exibirFrameReferenciar)

		# Instanciando o objeto a classe
		btn_botaoConfigurar = QPushButton('Configurar', self)
		btn_botaoConfigurar.setFont(fonteBotao)
		btn_botaoConfigurar.setGeometry(offSetBotaoPrincila + botaoWSize * 2, 150, botaoWSize, botaoHSize)

		btn_botaoConfigurar.clicked.connect(self.exibirFrameConfigurar)

		# Instanciando o objeto a classe
		btn_botaoAjuda = QPushButton('Ajuda', self)
		btn_botaoAjuda.setFont(fonteBotao)
		btn_botaoAjuda.setGeometry(offSetBotaoPrincila + botaoWSize * 3, 150, botaoWSize, botaoHSize)

		btn_botaoAjuda.clicked.connect(self.exibirFrameAJuda)

	def framesJanelaPrincipal(self):
		estiloFrames = """
						background-color: white;
						border: 15px solid rgb(237, 237, 237);
		"""

		estiloBotoesFrames = """
						QPushButton {
						   	background-color: blue;
						   	color: white;
						   	border: 2px solid blue;
						   	border-radius: 10px;
					  	}
					   	QPushButton:hover{
					   		background-color: white;
						   	color: blue;
						   	border: 2px solid blue;
						   	border-radius: 10px;
					   	}
					   	QPushButton:pressed{
						   	background-color: white;
						   	color:black;
					   	}
		"""

		# Declarando que iremos utilizar as variaveis globais e não locais
		global frameWSize, frameHSize, frameXPosition, frameYPosition
		# -------------------------FRAME IMPRIMIR------------------------------------
		global frm_Imprimir
		frm_Imprimir = QFrame(self)
		frm_Imprimir.setGeometry(frameXPosition, frameYPosition, frameWSize, frameHSize)
		frm_Imprimir.setAutoFillBackground(True)
		frm_Imprimir.setStyleSheet(estiloFrames)
		frm_Imprimir.setVisible(False)

		btn_iniciarImpressao = QPushButton('Iniciar', frm_Imprimir)
		btn_iniciarImpressao.setFont(fonteBotao)
		btn_iniciarImpressao.setGeometry(20, 20, 150, 50)
		btn_iniciarImpressao.setStyleSheet(estiloBotoesFrames)

		# -------------------------FRAME REFERENCIAR---------------------------------
		global frm_Referenciar
		frm_Referenciar = QFrame(self)
		frm_Referenciar.setGeometry(frameXPosition, frameYPosition, frameWSize, frameHSize)
		frm_Referenciar.setAutoFillBackground(True)
		frm_Referenciar.setStyleSheet(estiloFrames)
		frm_Referenciar.setVisible(False)
		# -------------------------FRAME CONFIGURAR----------------------------------
		global frm_Configurar
		frm_Configurar = QFrame(self)
		frm_Configurar.setGeometry(frameXPosition, frameYPosition, frameWSize, frameHSize)
		frm_Configurar.setAutoFillBackground(True)
		frm_Configurar.setStyleSheet(estiloFrames)
		frm_Configurar.setVisible(False)
		# -------------------------FRAME AJUDA---------------------------------------
		global frm_Ajuda
		frm_Ajuda = QFrame(self)
		frm_Ajuda.setGeometry(frameXPosition, frameYPosition, frameWSize, frameHSize)
		frm_Ajuda.setAutoFillBackground(True)
		frm_Ajuda.setStyleSheet(estiloFrames)
		frm_Ajuda.setVisible(False)

		# -------------------------BACKGROUND---------------------------------------
		global frm_background
		frm_background = QFrame(self)
		frm_background.setGeometry(frameXPosition, frameYPosition, frameWSize, frameHSize)
		frm_background.setStyleSheet("""
		background-color: black
		""")
		frm_background.setVisible(True)

	def exibirFrameImprimir(self):
		allFramesInvisible()
		frm_Imprimir.setVisible(True)
		print('Frame imprimir!')

	# -------------------------FRAME REFERENCIAR---------------------------------
	def exibirFrameReferenciar(self):
		allFramesInvisible()
		frm_Referenciar.setVisible(True)
		print('Frame Referenciar!')

	# -------------------------FRAME CONFIGURAR----------------------------------
	def exibirFrameConfigurar(self):
		allFramesInvisible()
		frm_Configurar.setVisible(True)
		print('Frame Configurar!')

	# -------------------------FRAME AJUDA---------------------------------------
	def exibirFrameAJuda(self):
		allFramesInvisible()
		frm_Ajuda.setVisible(True)
		print('Frame Ajuda')


def allFramesInvisible():
	frm_Imprimir.setVisible(False)
	frm_Referenciar.setVisible(False)
	frm_Configurar.setVisible(False)
	frm_Ajuda.setVisible(False)
	frm_background.setVisible(False)


def principalExecutar():
	app = QApplication.instance()
	if app is None:
		app = QApplication(sys.argv)
	principal = janelaPrincipal()
	principal.show()
	app.exec()


principalExecutar()
