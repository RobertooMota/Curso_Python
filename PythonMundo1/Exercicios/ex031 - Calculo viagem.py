distancia = float(input('Qual a distancia da viagem? '))
if distancia < 200.00:
    print('O valor da sua passagem será de: R$ {}'.format(distancia * 0.50))
else:
    print('O valor da sua passagem será de: R$ {}'.format(distancia * 0.45))
