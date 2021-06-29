

while True:
    valor = int(input('\nEscolha um valor para a tabuada: '))
    if valor < 0:
        print(f'Programa finalizado.\nValor digitado: {valor}')
        break
    else:
        for i in range(0, 10 + 1):
            print(f'{i} * {valor} = {i * valor}')