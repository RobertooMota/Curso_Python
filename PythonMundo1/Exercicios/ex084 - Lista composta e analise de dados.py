pessoa = list()
total = list()
cadastro = 1

maiorPeso = menorPeso = 0

while cadastro:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))

    if len(total) == 0:
        maiorPeso = pessoa[1]
        menorPeso = pessoa[1]
    else:
        if pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]
        if pessoa[1] < menorPeso:
            menorPeso = pessoa[1]

    total.append(pessoa[:])
    pessoa.clear()
    print(f'Maior = {maiorPeso}, menor = {menorPeso}')
    res = str(input('Deseja continuar? [S/N]'))
    if res not in 'sS':
        cadastro = 0

print(f'Ao todo foram cadastradas {len(total)} pessoas!')
print(f'Maior pesso foi de: {maiorPeso}kg. De', end=' ')
for i in total:
    if i[1] == maiorPeso:
        print(i[0], end=' ')
print('')
print(f'Menor pesso foi de: {menorPeso}kg. De', end='')
for i in total:
    if i[1] == menorPeso:
        print(i[0], end=' ')

