import random

nome1 = input('Nome do aluno: ')
nome2 = input('Nome do aluno: ')
nome3 = input('Nome do aluno: ')
nome4 = input('Nome do aluno: ')

lista = [nome1, nome4, nome3, nome2]


print('Aluno sorteado: {}'.format(random.choice(lista)))
