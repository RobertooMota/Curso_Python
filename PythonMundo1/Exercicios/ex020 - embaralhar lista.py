#shuffle embaralha o que esta se colocando como parametro


from random import shuffle

nome1 = input('Nome do aluno: ')
nome2 = input('Nome do aluno: ')
nome3 = input('Nome do aluno: ')
nome4 = input('Nome do aluno: ')

lista = [nome1, nome4, nome3, nome2]
shuffle(lista)

print('Aluno sorteado: {}'.format(lista))
