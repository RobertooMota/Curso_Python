# 1234
valor = int(input('Insira um valor entre 0 e 9999: '))
u = int(valor // 1 % 10)
d = int(valor // 10 % 10)
c = int(valor // 100 % 10)
m = int(valor // 1000 % 10)

print('Resultado do numero: {}'.format(valor))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(u, d, c, m))
