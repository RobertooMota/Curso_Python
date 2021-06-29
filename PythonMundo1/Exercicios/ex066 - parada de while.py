count = 0
soma = 0
numero = 0

while True:
    numero = int(input('Digite um numero: '))

    if numero == 999:
        break
    else:
        soma += numero
        count += 1


print(f'Foram digitados {count} numeros e a soma deles é de {soma}')
