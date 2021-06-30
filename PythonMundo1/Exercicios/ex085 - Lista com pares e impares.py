valores = [[], []]
valor = 0
for i in range(0, 7):

    valor = int(input('Digite um valor: '))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
print(f'Valore pares: {valores[0]}')
valores[1].sort()
print(f'Valore impares: {valores[1]}')
