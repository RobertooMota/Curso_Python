#Programa que converte um numero para a base escolhida pelo usuario

valor = int(input('Digite um valor para ser convertido: '))
escolha = int(input('Escolha a base: 1-BIN    2-OCT   3-HEX --->>>> '))

if escolha > 3 or escolha < 1:
    print('Você escolheu uma opção que não temos no menu! tente novamente!')
elif escolha == 1:
    valorBin = bin(valor)
    valorBin.split()
    print('O numero {} em binário é: {}'.format(valor, valorBin[2:]))
elif escolha == 2:
    valorOct = oct(valor)
    valorOct.split()
    print('O numero {} em octal é: {}'.format(valor, valorOct[2:]))
else:
    valorHex = hex(valor)
    valorHex.split()
    print('O numero {} em Hexadecimal é: {}'.format(valor, valorHex[2:]))