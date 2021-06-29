lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))

    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta not in 'sS':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Numeros digitados: {lista}')
print(f'Lista de numeros pares: {pares}')
print(f'Lista de numeros impares: {impares}')

