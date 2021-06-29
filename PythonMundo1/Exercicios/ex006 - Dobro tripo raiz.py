from cmath import sqrt

num = int(input('Digite um numero: '))

print('O dobro {}, triplo {}, raiz quadrada {:.4}!'.format(num * 2, num * 3, (num ** (1 / 2))))
print('Raiz quadrada de outra forma {:.4}'.format(sqrt(num)))
