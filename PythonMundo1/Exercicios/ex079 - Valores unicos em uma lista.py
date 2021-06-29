numeros = []

while True:

    valor = (int(input('Digite um valor para adicionar a lista: ')))
    if valor not in numeros:
        numeros.append(valor)
        print(f'Valor {valor} salvo com sucesso!')
    else:
        print('Valor existente!')
    continuar = str(input('Deseja continuar? [S/N] ')).upper()

    if continuar.upper() != 'S' and continuar != 'SIM':
        print(continuar)
        break
numeros.sort()
print(f'Os numeros digitados foram: {numeros}')
