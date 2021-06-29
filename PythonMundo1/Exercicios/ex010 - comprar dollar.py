num = int(input('Quanto dinheiro tem: '))
valor_uss = int(3.27)
cambio = num / valor_uss
print('Com R${} é possivel comprar U$${:.3}!'.format(num, cambio))
