# formula para IMC = peso / altura²

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print('Abaixo do peso ideal!')
elif 18.5 <= IMC < 25:
    print('Peso ideal!')
elif 25 <= IMC < 30:
    print('Sobrepeso!')
elif 30 <= IMC < 40:
    print('Obesidade!!!!')
else:
    print('Obesidade Morbida!!!!!!')
