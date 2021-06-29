# calcula o desconto do produto de acordo com a forma de pagamento!

valorProduto = float(input('Informe o valor do produto R$ '))
modoPagamento = int(input('''Modo de pagamento:
1 - à vista / Cheque  
2 - à vista no cartão 
3 - 2x no cartão 
4 - 3x ou mais no cartão 
'''))

if 0 < modoPagamento <= 4:
    if modoPagamento == 1:
        print('Valor do produto R$ {:.2f} (10% de desconto) '.format(valorProduto * (1 - 0.10)))
    if modoPagamento == 2:
        print('Valor do produto R$ {:.2f} (5% de desconto) '.format(valorProduto * (1 - 0.05)))
    if modoPagamento == 3:
        print('Valor do produto R$ {:.2f} (Sem desconto) '.format(valorProduto))
    if modoPagamento == 4:
        print('Valor do produto R$ {:.2f} (20% de Juros!) '.format(valorProduto * 1.2))
else:
    print('Opção invalida!')
