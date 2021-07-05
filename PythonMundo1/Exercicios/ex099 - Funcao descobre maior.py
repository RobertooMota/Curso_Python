def separador():
    print('~' * 30)


def maior(values):
    maiorNum = max(values)
    return maiorNum


num = list()
count = 0
while count < 5:
    num.append(int(input('Digita um valor: ')))
    count += 1

print(f'Foram informados {len(num)} valores. O maior valor digitado foi {maior(num)}.')
maior(num)

