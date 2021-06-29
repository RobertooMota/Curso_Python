velocidade = int(input('Qual foi a velocidade? '))
maxVel = int(80)
valorMulta = int(7)
if velocidade > maxVel:
    multa = int((velocidade - maxVel) * valorMulta)
    print('Velocidade excedida! Multa no valor de R$ {:.2f}.'.format(multa))
else:
    print('Velocidade dentro do permitido!')
