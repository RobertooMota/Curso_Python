import main as m
import janela2 as p
import sys


def carregaSist():
	OPEN = m.execution()
	print(OPEN)

	if OPEN == 'open janela 2':
		p.execution()


carregaSist()
sys.exit()
