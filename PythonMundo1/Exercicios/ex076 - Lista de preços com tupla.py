lista = ('Caderno', 20, 'Lapis', 1.30, 'caneta', 7, 'estojo', 2, 'borracha', 0.50)
tabulacao = 20
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f' R$ {float(lista[i])}')
