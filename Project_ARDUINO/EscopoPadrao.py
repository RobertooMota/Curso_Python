from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QFont, QIcon, QTextLine
import sys

sub = 'HELLOW WORLD'


class mainWindow(QWidget):
	def __init__(self):
		super().__init__()
		# Configurações da janela
		# Tamanho e posição
		self.setFixedSize(600, 600)
		self.setWindowTitle(f'Arduino: {sub}')


def execution():
	app = QApplication.instance()
	if app is None:
		app = QApplication(sys.argv)
	janela = mainWindow()
	janela.show()
	app.exec()


execution()
