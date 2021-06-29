nome = input('Digite uma palavra ou frase: ').upper().strip()
print('A letra "A" aparece: {}'.format(nome.count('A')))
print('Aparece a primeira vez na posição: {}'.format(nome.find('A') + 1))
print('Aparece a ultima vez na posição: {}' .format(nome.rfind('A') + 1))

