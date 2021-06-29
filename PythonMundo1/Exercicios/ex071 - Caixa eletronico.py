valorSacado = int(input('Valor a ser sacado R$ '))
print('')
sobra = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

while True:
    print('#' * 30)
    if valorSacado // 50 > 0:
        print(f'Total de {valorSacado // 50} notas de R$ 50')
        valorSacado = valorSacado % 50
    if valorSacado // 20 > 0:
        print(f'Total de {valorSacado // 20} notas de R$ 20')
        valorSacado = valorSacado % 20
    if valorSacado // 10 > 0:
        print(f'Total de {valorSacado // 10} notas de R$ 10')
        valorSacado = valorSacado % 10
    if valorSacado // 1 > 0:
        print(f'Total de {valorSacado // 1} notas de R$ 1')
        valorSacado = valorSacado % 1
    print('#' * 30)
    break

