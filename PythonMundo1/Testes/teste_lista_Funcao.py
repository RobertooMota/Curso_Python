def relistar(doc):
	lista = list()
	listaFinal = list()
	adicionar = True
	comparador = ''
	for i in doc:
		lista.append(i.rstrip())

	for item in lista:
		adicionar = True
		for x in range(0, 4):
			comparador += item[x]

		if len(listaFinal) == 0:
			listaFinal.append(item)
		else:
			for itens in listaFinal:
				print(f'{comparador} - {itens} - {adicionar}')
				if comparador in itens:
					adicionar = False

			if adicionar:
				listaFinal.append(item)

		comparador = ''
	print(listaFinal)


documento = open('lista.txt', 'r')
relistar(documento)
