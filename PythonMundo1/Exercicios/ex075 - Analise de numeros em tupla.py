numeros = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')),
           int(input('Digite um numero: ')))
pares = 0

if 9 in numeros:
    print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
else:
    print('Não foi digitado numero 9')

if 3 in numeros:
    print(f'A primeira vez que o valor 3 foi digitado foi: {numeros.index(3)+1}')
else:
    print('Não foi digitado numero 3!')

for teste in numeros:
    if teste % 2 == 0:
        pares += 1

if pares > 0:
    print(f'Foram digitados {pares} numeros pares.')
else:
    print('Não foi digitado numeros pares!')
