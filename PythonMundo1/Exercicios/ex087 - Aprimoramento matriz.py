# Nesse caso inserimos valores a matriz para que ela já tenha um tamanho definido
# Sendo assim, em vez de dar .append, podemos simplesmente fazer atribuição
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma3Col = 0
maior2Lin = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Insira um valor: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ] ', end='')  #:^5 = 5 espaços , ^ = centralizado
    print('')

for linha in range(0, 3):
    for coluna in range(0, 3):
        soma += matriz[linha][coluna]
print(f'\nO valor da somatoria da matriz é {soma}')

for i in range(0, 3):
    soma3Col += matriz[i][2]
print(f'A soma dos valores da 3 coluna é {soma3Col}')

for i in range(0, 3):
    if i == 0:
        maior2Lin = matriz[1][i]
    elif matriz[1][i] > maior2Lin:
        maior2Lin = matriz[1][i]
print(f'O maior valor da linha 2 é {maior2Lin}')


