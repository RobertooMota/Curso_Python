nome = input('Digite seu nome completo: ')
print('Todas em Maiusculas: {}'.format(nome.upper()))
print('Todas em Minusculas: {}'.format(nome.lower()))
print('Quantidade de letrase sem espaço: {}'.format(len(nome.replace(' ', '').strip())))
nomeSplitado = nome.split()
print(len(nomeSplitado[0]))
