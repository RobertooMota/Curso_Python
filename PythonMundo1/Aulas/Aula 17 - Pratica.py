valores = []
for i in range(0,10):
    valores.append(i)
print('Fim do for com APPEND')

valores.sort(reverse=True)
for pos, value in enumerate(valores):
    print(f'Na posicao {pos}, temos o valor: {value}')
print('Fim do Programa!')
