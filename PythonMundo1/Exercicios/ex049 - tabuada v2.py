# o usuario escolhe um numero e é mostrado a tabuada para ele

valor = int(input('Escolha um valor para a tabuada: '))
for i in range(0, 10 + 1):
    print('{} * {} = {}'.format(i, valor, i * valor))
