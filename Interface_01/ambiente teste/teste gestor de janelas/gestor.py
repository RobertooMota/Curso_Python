import janela1 as jn1
import janela2 as jn2


def software():
	while True:
		reposta = str(input('Qual janela abrir? ')).upper()
		if reposta == 'JANELA 1':
			jn1.executar()
		elif reposta == 'JANELA 2':
			jn2.executar()
		elif reposta == 'PARAR':
			print('Programa finalizado')
			break
		else:
			print('Opcoes incorretas')


software()
