nome = input('Digite seu nome completo: ').strip()
nomeLista = nome.split()
print('Ola {} {}!!!'.format(nomeLista[0], nomeLista[len(nomeLista)-1]))
