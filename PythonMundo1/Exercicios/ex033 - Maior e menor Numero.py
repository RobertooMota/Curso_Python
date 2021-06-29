val1 = int(input('Digite o valor 1: '))
val2 = int(input('Digite o valor 2: '))
val3 = int(input('Digite o valor 3: '))

if val1 > val2 and val1 > val3:
    print('O maior valor é o {}.'.format(val1))
if val2 > val3:
    print('O maior valor é o {}.'.format(val2))
else:
    print('O maior valor é o {}.'.format(val3))


if val1 < val2 and val1 < val3:
    print('O menor valor é o {}.'.format(val1))
else:
    if val2 < val3 and val2 < val1:
        print('O menor valor é o {}.'.format(val2))
    else:
        print('O menor valor é o {}.'.format(val3))