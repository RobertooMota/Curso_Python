salario = float(input('Digite o valor do salario: '))
salarioBase = float(1250.00)
if salario <= salarioBase:
    print('O novo salario será de: R$ {}'.format(salario*1.15))
else:
    print('O novo salario será de: R$ {}'.format(salario * 1.10))
