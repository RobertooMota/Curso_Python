#compara dois valores de entrada e diz qual é maior ou se são iguais

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro numero é maior!')
elif num2 > num1:
    print('O segundo numero é maior!')
else:
    print('Os numeros são iguais!')