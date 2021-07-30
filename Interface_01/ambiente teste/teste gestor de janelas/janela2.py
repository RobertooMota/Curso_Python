from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys
import janela1 as jn1


class tela_2(QWidget):
	def __init__(self):
		super().__init__()

		self.setFixedSize(500, 500)
		self.botao()

	def botao(self):
		bt = QPushButton('BOTAO', self)
		bt.move(200, 200)
		bt.clicked.connect(self.botaoClicado)

	def botaoClicado(self):
		print('clicou tela 2')


def executar():
	app = QApplication.instance()
	if app is None:
		app = QApplication(sys.argv)
	janela1 = tela_2()
	janela1.show()
	app.exec()
