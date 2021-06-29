altura = int(input('Altura da parede em metros: '))
largura = int(input('Largura da parede em metros: '))
rendimento = int(2)

print('Será necessário {} litros de tinta para pintar sua parade, que possui {} m².'.format(
    (largura * altura) / rendimento, altura * largura))
