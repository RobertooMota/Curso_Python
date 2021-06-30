# Nesse caso inserimos valores a matriz para que ela já tenha um tamanho definido
# Sendo assim, em vez de dar .append, podemos simplesmente fazer atribuição
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Insira um valor: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ] ', end='')  #:^5 = 5 espaços , ^ = centralizado
    print('')
