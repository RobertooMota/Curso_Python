numeros = []
maior = 0
menor = 0
count = 0
while count < 5:

    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        if valor > maior:
            numeros.append(valor)
            print(f'Salvo na posicao: {numeros.index(max(numeros))} ')
            maior = valor
            count += 1
            if menor == 0:
                menor = valor
        elif valor < menor:
            print(f'Salvo na posicao: {numeros.index(min(numeros))} ')
            numeros.insert(numeros.index(min(numeros)), valor)
            menor = valor
            count += 1
        else:
            for i in range(0, len(numeros)):
                if valor < numeros[i]:
                    numeros.insert(numeros.index(numeros[i]), valor)
                    print(f'Salvo na posicao: {numeros.index(numeros[i])}')
                    break
            count += 1

    else:
        print('Valor existente!')
for pos, i in enumerate(numeros):
    print(f'Numero {i} salvo na posicao {pos}')
