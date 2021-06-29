#programa para analisar se libera emprestimo para compra de imovel
#   salario = 100
#   prestacao = x
#   x = (100 * prestacao) / salario


valorCasa = float(input('Qual é o valor da casa em R$? '))
salarioComprador = float(input('Qual é o salario do comprador? '))
tempoPagamento = int(input('Em quantos anos pretende pagar? '))

mesesPagamento = tempoPagamento * 12
prestacaoMensal = valorCasa / mesesPagamento
PorcentagemAtual = (100 * prestacaoMensal) / salarioComprador
parcelaMaximaPossivel = salarioComprador * 0.3

if prestacaoMensal > parcelaMaximaPossivel:
    print('Emprestimo negado! O valor mensal atual corresponde a {:.2f}% do seu salário!'.format(PorcentagemAtual))
else:
    print('Emprestimo liberado! O valor da mensalidade corresponde a {}% do seu salario!'.format(PorcentagemAtual))
