dias = int(input('Dias em que se utilizou do carro: '))
km = float(input('Km rodados: '))
valorDia = int (60)
valorKm = float(0.15)

custo = (dias*valorDia) + (km+valorKm)
print('Valor a ser pago é de: R$ {}.'.format(custo))
